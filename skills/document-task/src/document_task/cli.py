import argparse
import json
import sys

from . import task
from .errors import DocumentTaskError


def emit(data) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="document-task")
    sub = parser.add_subparsers(dest="action", required=True)

    p_prepare = sub.add_parser("prepare")
    p_prepare.add_argument("source")

    p_process = sub.add_parser("process")
    p_process.add_argument("document_id")
    p_process.add_argument("instruction")
    p_process.add_argument("--output", required=True)

    p_resume = sub.add_parser("resume")
    p_resume.add_argument("task_id")

    p_status = sub.add_parser("status")
    p_status.add_argument("task_id")

    p_finalize = sub.add_parser("finalize")
    p_finalize.add_argument("task_id")

    p_finding = sub.add_parser("append-finding")
    p_finding.add_argument("task_id")
    p_finding.add_argument("section_id")
    p_finding.add_argument("text")

    args = parser.parse_args(argv)
    try:
        if args.action == "prepare":
            emit(task.prepare(args.source))
        elif args.action == "process":
            emit(task.create_or_advance(args.document_id, args.instruction, args.output))
        elif args.action == "resume":
            emit(task.resume(args.task_id))
        elif args.action == "status":
            emit(task.status(args.task_id))
        elif args.action == "finalize":
            emit(task.finalize(args.task_id))
        elif args.action == "append-finding":
            emit(task.record_finding(args.task_id, args.section_id, args.text))
        return 0
    except DocumentTaskError as exc:
        emit({"status": "error", "code": exc.code, "message": str(exc)[:240]})
        return 2
    except Exception as exc:
        emit({"status": "error", "code": "UNEXPECTED_ERROR", "message": str(exc)[:240]})
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
