from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from db.config import settings
from mediafusion_scrapy.task import run_spider
from utils.validation_helper import validate_tv_streams_in_db


def setup_scheduler(scheduler: AsyncIOScheduler):
    """
    Set up the scheduler with the required jobs.
    """
    # Setup tamil blasters scraper
    if not settings.disable_tamil_blasters_scheduler:
        scheduler.add_job(
            run_spider.send,
            CronTrigger.from_crontab(settings.tamil_blasters_scheduler_crontab),
            name="tamil_blasters",
            kwargs={
                "spider_name": "tamil_blasters",
                "crontab_expression": settings.tamil_blasters_scheduler_crontab,
            },
        )

    # Setup tamilmv scraper
    if not settings.disable_tamilmv_scheduler:
        scheduler.add_job(
            run_spider.send,
            CronTrigger.from_crontab(settings.tamilmv_scheduler_crontab),
            name="tamilmv",
            kwargs={
                "spider_name": "tamilmv",
                "crontab_expression": settings.tamilmv_scheduler_crontab,
            },
        )

    # Setup formula_tgx scraper
    if not settings.disable_formula_tgx_scheduler:
        scheduler.add_job(
            run_spider.send,
            CronTrigger.from_crontab(settings.formula_tgx_scheduler_crontab),
            name="formula_tgx",
            kwargs={
                "spider_name": "formula_tgx",
                "scrape_all": "false",
                "crontab_expression": settings.formula_tgx_scheduler_crontab,
            },
        )

    # Setup mhdtvworld scraper
    if not settings.disable_mhdtvworld_scheduler:
        scheduler.add_job(
            run_spider.send,
            CronTrigger.from_crontab(settings.mhdtvworld_scheduler_crontab),
            name="mhdtvworld",
            kwargs={
                "spider_name": "mhdtvworld",
                "crontab_expression": settings.mhdtvworld_scheduler_crontab,
            },
        )

    # Setup mhdtvsports scraper
    if not settings.disable_mhdtvsports_scheduler:
        scheduler.add_job(
            run_spider.send,
            CronTrigger.from_crontab(settings.mhdtvsports_scheduler_crontab),
            name="mhdtvsports",
            kwargs={
                "spider_name": "mhdtvsports",
                "crontab_expression": settings.mhdtvsports_scheduler_crontab,
            },
        )

    # Setup tamilultra scraper
    if not settings.disable_tamilultra_scheduler:
        scheduler.add_job(
            run_spider.send,
            CronTrigger.from_crontab(settings.tamilultra_scheduler_crontab),
            name="tamilultra",
            kwargs={
                "spider_name": "tamilultra",
                "crontab_expression": settings.tamilultra_scheduler_crontab,
            },
        )

    # Schedule validate_tv_streams_in_db
    if not settings.disable_validate_tv_streams_in_db:
        scheduler.add_job(
            validate_tv_streams_in_db.send,
            CronTrigger.from_crontab(settings.validate_tv_streams_in_db_crontab),
            name="validate_tv_streams_in_db",
            kwargs={"crontab_expression": settings.validate_tv_streams_in_db_crontab},
        )

    # Schedule sport_video scraper
    if not settings.disable_sport_video_scheduler:
        scheduler.add_job(
            run_spider.send,
            CronTrigger.from_crontab(settings.sport_video_scheduler_crontab),
            name="sport_video",
            kwargs={
                "spider_name": "sport_video",
                "scrape_all": "false",
                "crontab_expression": settings.sport_video_scheduler_crontab,
            },
        )

    # Schedule streamed scraper
    if not settings.disable_streamed_scheduler:
        scheduler.add_job(
            run_spider.send,
            CronTrigger.from_crontab(settings.streamed_scheduler_crontab),
            name="streamed",
            kwargs={
                "spider_name": "streamed",
                "crontab_expression": settings.streamed_scheduler_crontab,
            },
        )

    # Schedule mrgamingstreams scraper
    if not settings.disable_mrgamingstreams_scheduler:
        scheduler.add_job(
            run_spider.send,
            CronTrigger.from_crontab(settings.mrgamingstreams_scheduler_crontab),
            name="mrgamingstreams",
            kwargs={
                "spider_name": "mrgamingstreams",
                "crontab_expression": settings.mrgamingstreams_scheduler_crontab,
            },
        )

    # Schedule crictime scraper
    if not settings.disable_crictime_scheduler:
        scheduler.add_job(
            run_spider.send,
            CronTrigger.from_crontab(settings.crictime_scheduler_crontab),
            name="crictime",
            kwargs={
                "spider_name": "crictime",
                "crontab_expression": settings.crictime_scheduler_crontab,
            },
        )

    # Schedule streambtw scraper
    if not settings.disable_streambtw_scheduler:
        scheduler.add_job(
            run_spider.send,
            CronTrigger.from_crontab(settings.streambtw_scheduler_crontab),
            name="streambtw",
            kwargs={
                "spider_name": "streambtw",
                "crontab_expression": settings.streambtw_scheduler_crontab,
            },
        )

    # Schedule dlhd scraper
    if not settings.disable_dlhd_scheduler:
        scheduler.add_job(
            run_spider.send,
            CronTrigger.from_crontab(settings.dlhd_scheduler_crontab),
            name="dlhd",
            kwargs={
                "spider_name": "dlhd",
                "crontab_expression": settings.dlhd_scheduler_crontab,
            },
        )
