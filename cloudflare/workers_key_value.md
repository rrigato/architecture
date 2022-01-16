Cloudflare workers key value store = edge key value store that supports 512 byte keys and 25 mb values

- eventually consistent with **last writer wins** conflict resolution

- workers key value is better for static content and configuration that is needed globally and rarely changes
- workers durable objects is better for dynamic state and coordination
