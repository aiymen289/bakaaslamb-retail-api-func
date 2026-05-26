from dataclasses import dataclass
from typing import Optional

@dataclass
class ConfigThresholds:
    expiring_soon_days: int = 7
    stockout_risk_doc: float = 3.0
    high_stock_doc: float = 30.0

@dataclass
class ConfigFormulas:
    markdown: str = "standard"
    markdown_elasticity: float = 1.5

@dataclass
class Config:
    thresholds: ConfigThresholds = None
    formulas: ConfigFormulas = None

    def __post_init__(self):
        if self.thresholds is None:
            self.thresholds = ConfigThresholds()
        if self.formulas is None:
            self.formulas = ConfigFormulas()

@dataclass
class MetricPanel:
    metric_name: str = ""
    value: str = ""
    count: int = 0
    badge_type: str = ""
    amount: Optional[str] = None

@dataclass
class DashboardMetrics:
    expiring_soon: MetricPanel = None
    stockout_risk: MetricPanel = None
    waste_today: Optional[MetricPanel] = None
    gross_profit: Optional[MetricPanel] = None
    sales_today: Optional[MetricPanel] = None

@dataclass
class InventoryItemDetail:
    batch_code: str = ""
    product_name: str = ""
    category: str = ""
    quantity: int = 0
    expiry_date: str = ""
    days_until_expiry: int = 0
    cost_price: float = 0.0
    retail_price: float = 0.0
    gross_profit_per_unit: float = 0.0
    gross_profit_total: float = 0.0
    average_daily_sales: float = 0.0
    days_of_coverage: float = 0.0
    quantity_at_risk: int = 0
    suggested_markdown_percent: float = 0.0

@dataclass
class ActivityEvent:
    event_type: str = ""
    title: str = ""
    description: str = ""
    transaction_id: str = ""
    timestamp: str = ""
    amount: Optional[str] = None
    icon_color: str = ""