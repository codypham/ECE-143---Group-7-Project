from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_states import data as states
from bokeh.models import BasicTicker, ColorBar, LogColorMapper, PrintfTickFormatter
import pandas as pd
from bokeh.palettes import Viridis6 as palette

def Bokeh_Map(value='ADJUSTED INCOME'):
    '''
    This function produces interactive maps using bokeh. The map shows US states in 6 different colors with data from the column named value from analysis.tsv.
    :param value: value can be "TAX","COST OF LIVING","SALARY","ADJUSTED INCOME". Default is "Adjusted Income"
    :return: p (bokeh figure): a bokeh interactive map
    '''
    assert isinstance(value,str)
    # import data
    df = pd.read_csv('../data/data_analysis.tsv', sep='\t')
    # fomat new sourcedata for map
    lons = []
    lats = []
    for index, name in df.iterrows():
        flag = False
        for code in states:
            if code == name['CODE']:
                lons.append(states[code]["lons"])
                lats.append(states[code]["lats"])
                flag = True
        if flag == False:
            lons.append(0)
            lats.append(0)
    df['lons'] = lons
    df['lats'] = lats

    data = dict(
        x=lons,
        y=lats,
        name=df['CODE'].tolist(),
        values=df[value].tolist(),
    )

    mapper = LogColorMapper(palette=palette)

    TOOLS = "pan,wheel_zoom,reset,hover,save"

    p = figure(title=f"IDEAL PLACE TO LIVE IN TERMS OF {value}", tools=TOOLS,
               x_axis_location=None, y_axis_location=None,
               tooltips=[("Name", "@name"), (value, "@values"), ("(Long, Lat)", "($x, $y)")],
               toolbar_location="left",
               plot_width=3400, plot_height=700)

    p.grid.grid_line_color = None
    p.hover.point_policy = "follow_mouse"

    p.patches('x', 'y', source=data,
              fill_color={'field': 'values', 'transform': mapper}, fill_alpha=0.7,
              line_color='black', line_width=0.5,)

    color_bar = ColorBar(color_mapper=mapper, location=(-3300, 0),
                         ticker=BasicTicker(desired_num_ticks=6),
                         formatter=PrintfTickFormatter(format="%d%%"))

    p.add_layout(color_bar, 'right')
    output_file(f"Bokeh_{value}.html", title="IDEAL PLACE TO LIVE")
    show(p)
    return p


if __name__ == '__main__':
    for value in ["TAX","COST OF LIVING","SALARY","ADJUSTED INCOME"]:
        Bokeh_Map(value)
