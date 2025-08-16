from pyecharts import options as opts  
from pyecharts.charts import Bar

# 准备数据
x_data = ['一月', '二月', '三月', '四月', '五月']
y_data = [10,20,15,25,30]

# 创建柱状图
bar_chart = Bar()
bar_chart.add_xaxis(x_data)
bar_chart.add_yaxia("销售额:",y_data)

# 配置全局属性
bar_chart.set_global_opts(
    title_opts = TitleOpts(title="月度销售额柱状图", subtitle="副标题"),
    xaxis_opts=opts.AxisOpts(name="月份")
)