/** @odoo-module **/

import { routerService } from "@web/core/browser/router_service";
import { jsonrpc } from "@web/core/network/rpc_service";
import { browser } from "@web/core/browser/browser";

async function sendActivity(hash) {
    try {
        if (hash && Object.keys(hash).length > 0) {
            await jsonrpc('/post/action_data', { data: hash });
        }
    } catch (err) {
        console.warn("Activity Log Error:", err);
    }
}

// Simple override
const originalStart = routerService.start;

routerService.start = function (env) {
    const router = originalStart.call(this, env);

    // Listen to route changes
    const originalPushState = router.pushState;
    const originalReplaceState = router.replaceState;

    router.pushState = function (hash, options) {
        const result = originalPushState.call(this, hash, options);
        sendActivity(router.current?.hash || hash);
        return result;
    };

    router.replaceState = function (hash, options) {
        const result = originalReplaceState.call(this, hash, options);
        sendActivity(router.current?.hash || hash);
        return result;
    };

    // Hash change listener
    browser.addEventListener("hashchange", () => {
        sendActivity(router.current?.hash);
    });

    return router;
};

export default routerService;