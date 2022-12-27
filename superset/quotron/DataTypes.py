
class Autocomplete:
    def __init__(self, question, email, time):
        self.question = question
        self.email = email
        self.time = time


class QuotronChart:
    def __init__(self, slice_name, viz_type, datasource_id, datasource_type, query_context, params ):
        self.slice_name = slice_name
        self.viz_type = viz_type
        self.datasource_id = datasource_id
        self.datasource_type = datasource_type
        self.query_context = query_context
        self.params = params



class Params:
    def __init__(self, datasource, viz_type, time_range, metrics, groupby, timeseries_limit_metric, order_desc):
        self.datasource = datasource
        self.viz_type = viz_type
        self.time_range = time_range
        self.metrics = metrics
        self.groupby=groupby
        self.timeseries_limit_metric=timeseries_limit_metric
        self.order_desc = order_desc



