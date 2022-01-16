
Cloudflare durable objects = instance of a Nodejs class that provides transactionally consistent key value storage

- each object has a globally unique id that other workers can reference 
- the state stored in the object is private which enables strong transactional consistency along with persistent storage
- you do not need to manage the region the durable object is stored in, cloudflare transparently manages moving durable objects between edge locations


# addressing_real_time_collaboration_between_users
- to enable real time communication between users A and B, you need a live coordination point where keystrokes from user A are immediately sent to and conflicts resolved by the coordination point so that user B can see the changes and vice versa
- A typical live coordination point is websockets where the safe source is stored in memory and then websockets can asyncronously persist to storage

- This architecture pattern enables real time collaboration and removes the need for clients to refresh/poll the server to obtain updates

- durable objects provides a live coordination point where CloudFlare will automatically use the edge point of presence closest to the user and migrate it as needed to minimize latency 


# use_cases
- shopping cart, IoT device coordination in a home, game server, live chat/comment widgets


# miscellaneous

Conflict-free Replicated Data Types (CRDT's) = allows users to make changes locally and handles the syncronization asyncronously using an automated algorithm for conflict resolution so all clients end up in the same state

- the idea behind durable objects is to avoid having to manage databases and regions when using state in serverless applications and transition to state representing the logical unit corresponding to the business domain (instead of caring about graphes/key value stores, we care about chat rooms in a chat app)
