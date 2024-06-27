from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
from datadog_api_client.v1.models import *

configuration = Configuration(
    api_key={
        'apiKeyAuth': '5b43606fe06d6e2d49e63f879543f4a3'
    },
    application_key={
        'appKeyAuth': '407f2e6a5d393dd0d5e0717a1d97c9692ab3e280'
    }
)

with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)

    # Define the dashboard
    dashboard = Dashboard(
        title="Lucas's Dashboard",
        widgets=[
            # Define your widgets here
            Widget(
                definition=WidgetDefinition(
                    type=WidgetDefinitionType("timeseries"),
                    requests=[
                        TimeseriesWidgetRequest(
                            q="avg:system.cpu.user{*}",
                            display_type="line",
                        ),
                    ],
                ),
            ),
            Widget(
                definition=WidgetDefinition(
                    type=WidgetDefinitionType("query_value"),
                    requests=[
                        QueryValueWidgetRequest(
                            q="avg:system.mem.used{*}",
                            aggregator="avg",
                        ),
                    ],
                ),
            ),
            Widget(
                definition=WidgetDefinition(
                    type=WidgetDefinitionType("toplist"),
                    requests=[
                        ToplistWidgetRequest(
                            q="top(system.disk.free{*}, 10, 'mean', 'desc')",
                        ),
                    ],
                ),
            ),
            Widget(
                definition=WidgetDefinition(
                    type=WidgetDefinitionType("heatmap"),
                    requests=[
                        HeatMapWidgetRequest(
                            q="avg:system.load.1{*} by {host}",
                        ),
                    ],
                ),
            ),
        ],
        layout_type=DashboardLayoutType("ordered"),
    )

    try:
        # Create the dashboard
        response = api_instance.create_dashboard(dashboard)
        print("Dashboard created with ID:", response.id)

        # Save the dashboard ID to a file
        with open("2-setup_datadog", "w") as f:
            f.write(response.id + "\n")

    except Exception as e:
        print("Exception when creating dashboard: %s\n" % e)
