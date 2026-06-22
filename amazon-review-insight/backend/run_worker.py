from __future__ import annotations

from redis import Redis
from rq import Connection, SimpleWorker

from backend.app.queueing import QUEUE_NAME, REDIS_URL


def main() -> None:
    connection = Redis.from_url(REDIS_URL)
    with Connection(connection):
        # SimpleWorker avoids the forked work-horse model that crashes on macOS
        # when Objective-C frameworks have been touched earlier in the process.
        worker = SimpleWorker([QUEUE_NAME])
        worker.work(with_scheduler=False)


if __name__ == "__main__":
    main()
