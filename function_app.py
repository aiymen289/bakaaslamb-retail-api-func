import azure.functions as func
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import ConfigManager
from engine import BusinessEngine

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config_manager = ConfigManager(os.path.join(BASE_DIR, "data", "config.json"))
current_config = config_manager.load()
business_engine = BusinessEngine(current_config, os.path.join(BASE_DIR, "data", "mock_data.json"))

def cors_headers():
    return {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "*",
        "Content-Type": "application/json"
    }

@app.route(route="health", methods=["GET"])
def health(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(json.dumps({"status": "ok", "service": "Retail OS Business Engine"}), headers=cors_headers())

@app.route(route="api/dashboard-metrics", methods=["GET"])
def dashboard_metrics(req: func.HttpRequest) -> func.HttpResponse:
    data = business_engine.get_dashboard_metrics()
    return func.HttpResponse(json.dumps(data, default=str), headers=cors_headers())

@app.route(route="api/inventory/all", methods=["GET"])
def inventory_all(req: func.HttpRequest) -> func.HttpResponse:
    data = business_engine.get_all_inventory_with_calculations()
    return func.HttpResponse(json.dumps([i.__dict__ if hasattr(i, '__dict__') else i for i in data], default=str), headers=cors_headers())

@app.route(route="api/inventory/expiring-soon", methods=["GET"])
def inventory_expiring(req: func.HttpRequest) -> func.HttpResponse:
    data = business_engine.get_expiring_soon_items()
    return func.HttpResponse(json.dumps([i.__dict__ if hasattr(i, '__dict__') else i for i in data], default=str), headers=cors_headers())

@app.route(route="api/inventory/stockout-risk", methods=["GET"])
def inventory_stockout(req: func.HttpRequest) -> func.HttpResponse:
    data = business_engine.get_stockout_risk_items()
    return func.HttpResponse(json.dumps([i.__dict__ if hasattr(i, '__dict__') else i for i in data], default=str), headers=cors_headers())

@app.route(route="api/activity-feed", methods=["GET"])
def activity_feed(req: func.HttpRequest) -> func.HttpResponse:
    data = business_engine.get_activity_feed()
    return func.HttpResponse(json.dumps([i.__dict__ if hasattr(i, '__dict__') else i for i in data], default=str), headers=cors_headers())

@app.route(route="api/config", methods=["GET"])
def get_config(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(json.dumps(config_manager.get_dict()), headers=cors_headers())

@app.route(route="api/profit-analysis", methods=["GET"])
def profit_analysis(req: func.HttpRequest) -> func.HttpResponse:
    data = business_engine.get_profit_analysis()
    return func.HttpResponse(json.dumps(data, default=str), headers=cors_headers())

@app.route(route="api/products", methods=["GET"])
def products(req: func.HttpRequest) -> func.HttpResponse:
    data = business_engine.get_products()
    return func.HttpResponse(json.dumps(data, default=str), headers=cors_headers())

@app.route(route="api/price-rules", methods=["GET"])
def price_rules(req: func.HttpRequest) -> func.HttpResponse:
    data = business_engine.get_price_rules()
    return func.HttpResponse(json.dumps(data, default=str), headers=cors_headers())

@app.route(route="api/recent-transactions", methods=["GET"])
def recent_transactions(req: func.HttpRequest) -> func.HttpResponse:
    data = business_engine.get_recent_transactions()
    return func.HttpResponse(json.dumps(data, default=str), headers=cors_headers())