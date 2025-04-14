from dagster import Definitions, load_assets_from_modules
from etl_pipeline_dagster.assets import prices, returns, news, report

all_assets = load_assets_from_modules([prices, returns, news, report])

defs = Definitions(assets=all_assets)
