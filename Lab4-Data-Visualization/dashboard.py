from dash import Dash, html, dcc, dependencies
import plotly.express as px
import pandas as pd

# 创建Dash应用程序对象
app = Dash(__name__)

# 读取数据集
df = pd.read_csv('./black-friday/BlackFriday.csv')

categories = sorted(set(df['Product_Category_1'].unique()) |
                    set(df['Product_Category_2'].unique()) |
                    set(df['Product_Category_3'].unique()))

categories = [cat for cat in categories if pd.notna(cat)]  # 去掉NAN值

genders = df['Gender'].unique()

cities = sorted(df['City_Category'].unique())

ages = sorted(df['Age'].unique())


# 定义生成购买总量按类别分组的函数
def generate_amount_category():
    category_amount = []

    for cat in categories:
        category_amount.append(
            len(df[df['Product_Category_1'] == cat]) +
            len(df[df['Product_Category_2'] == cat]) +
            len(df[df['Product_Category_3'] == cat]))

    category_amount_fr = pd.DataFrame({
        'Category': categories,
        'Amount': category_amount
    })

    fig = px.bar(category_amount_fr, x='Category', y='Amount',
                 color_discrete_sequence=["#6B81A3", "#CEE5EE", "#D0F0EE", "#97CBE7", "#9AEEDD"],
                 title='Purchase Amount for Each Category: ')

    fig.update_layout(xaxis={'dtick': 1}, title_font=dict(size=20))

    return fig


def generate_category_gender_pie():
    category_gender_amount = []

    for gen in genders:
        category_gender_amount.append(
            len(df[(df['Gender'] == gen)])
        )

    category_gender_amount_fr = pd.DataFrame({
        'Gender': genders,
        'Amount': category_gender_amount
    })

    fig = px.pie(category_gender_amount_fr, names='Gender', values='Amount',
                 color_discrete_sequence=["#6B81A3", "#CEE5EE", "#D0F0EE", "#97CBE7", "#9AEEDD"],
                 color='Gender',
                 title='Gender Proportion for Category All Categories :')

    fig.update_layout(title_font=dict(size=20))

    return fig


def generate_category_city_pie():
    category_city_amount = []

    for cit in cities:
        category_city_amount.append(
            len(df[(df['City_Category'] == cit)])
        )

    category_city_amount_fr = pd.DataFrame({
        'City_Category': cities,
        'Amount': category_city_amount
    })

    fig = px.pie(category_city_amount_fr, names='City_Category', values='Amount',
                 color_discrete_sequence=["#6B81A3", "#D0F0EE", "#CEE5EE", "#97CBE7", "#9AEEDD"],
                 color='City_Category',
                 title='City Proportion for All Categories :')

    fig.update_layout(title_font=dict(size=20))

    return fig


def generate_category_age_pie():
    category_age_amount = []

    for age in ages:
        category_age_amount.append(
            len(df[(df['Age'] == age)])
        )

    category_age_amount_fr = pd.DataFrame({
        'Age': ages,
        'Amount': category_age_amount
    })

    fig = px.line(category_age_amount_fr, x='Age', y='Amount',
                  color_discrete_sequence=["#6B81A3", "#CEE5EE", "#D0F0EE", "#97CBE7", "#9AEEDD"],
                  title='Age Proportion for All Categories :')

    fig.update_layout(title_font=dict(size=20))

    return fig


# 设置应用程序的布局，包括页面上不同部分的HTML元素和交互组件
app.layout = html.Div([
    # 页面标题
    html.Div(
        children=[
            html.H1(children='Black Friday Data Analysis Dashboard', style={
                'textAlign': 'center',
                'backgroundColor': '#CEE5EE'

            })
        ]
    ),

    # 每个类别的购买量-柱状图
    html.Div([
        html.H2(children='Customer Behavior Analysis by Product Category ', style={
            'textAlign': 'center',
            'backgroundColor': '#D0F0EE'
        }),
        html.Div([
            dcc.Graph(id='amount-category', figure=generate_amount_category())
        ])
        ,

        html.Div([
            # 对于某种特定的类别，它的购买者的性别饼图
            html.Div([
                dcc.Graph(id='category_gender-pie', figure=generate_category_gender_pie())
            ],
                style={'padding': '0px 5px', 'width': '33%', 'display': 'inline-block'}),
            # 对于某种特定的类别，它的购买者的城市饼图
            html.Div([
                dcc.Graph(id='category_city-pie', figure=generate_category_city_pie())
            ],
                style={'padding': '0px 5px', 'width': '33%', 'display': 'inline-block'}),
            # 对于某种特定的类别，它的购买者的年龄折线图
            html.Div([
                dcc.Graph(id='category_age-pie', figure=generate_category_age_pie())
            ],
                style={'padding': '0px 5px', 'width': '33%', 'display': 'inline-block'})
        ],
            style={
                'display': 'flex',
                'borderBottom': 'thin lightgrey solid',
                'backgroundColor': 'rgb(250, 250, 250)',
                'padding': '5px 5px'
            })],
        style={
            'borderBottom': 'thin lightgrey solid',
            'backgroundColor': 'rgb(250, 250, 250)',
            'paddingBottom': '20px'
        }
    ),

    # 性别/年龄比例分析部分
    html.H2(children='Customer Segmentation Analysis', style={
        'textAlign': 'center',
        'backgroundColor': '#D0F0EE'
    }),
    html.Div([
        html.Div([

            html.Div([
                # 性别下拉框

                # 城市下拉框
                html.Div([
                    html.H3(' Age :  ')],
                ),

                html.Div([
                    # 年龄段下拉框
                    dcc.Dropdown(
                        id='age-ranges',
                        options=[{'label': 'All', 'value': 'All'}] + [{'label': i, 'value': i} for i in ages],
                        value='All',
                        clearable=False)
                ],
                    style={'width': '35%', 'paddingTop': '13px', 'paddingLeft': '10px'}
                )],
                style={'display': 'flex', 'width': '100%'}
            ),
            html.Div([
                dcc.Graph(id='gender-ratio')],
                style={'width': '49%', 'display': 'inline-block', 'padding': '0px 5px'}
            ),
            html.Div([
                dcc.Graph(id='married-ratio')
            ],
                style={'width': '49%', 'display': 'inline-block', 'padding': '0px 5px'}
            )
        ],
            style={'width': '51%', 'display': 'inline-block', 'padding': '5px 5px'}
        ),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Gender :  ')],
                ),

                html.Div([
                    # 性别下拉框
                    dcc.Dropdown(
                        id='genders',
                        options=[{'label': 'All', 'value': 'All'}] + [{'label': i, 'value': i} for i in genders],
                        value='All',
                        clearable=False
                    )],
                    style={'width': '35%', 'paddingTop': '13px', 'paddingLeft': '10px', 'paddingRight': '30px'}),
                # 城市下拉框
                html.Div([
                    html.H3(' City_Category :  ')],
                ),

                html.Div([
                    dcc.Dropdown(
                        id='city-ratio',
                        options=[{'label': 'All', 'value': 'All'}] + [{'label': i, 'value': i} for i in cities],
                        value='All',
                        clearable=False
                    )],
                    style={'width': '35%', 'paddingTop': '13px', 'paddingLeft': '10px'}
                )],
                style={'display': 'flex', 'width': '100%'}
            ),
            # 年龄比例饼图
            dcc.Graph(id='age-ratio'),
        ],
            style={'width': '45%', 'display': 'inline-block', 'float': 'right'}
        ),
    ],
        style={
            'borderBottom': 'thin lightgrey solid',
            'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '5px 5px'
        }
    )])


@app.callback(
    dependencies.Output('category_gender-pie', 'figure'),
    dependencies.Input('amount-category', 'hoverData')
)
def update_category_gender_pie(hoverData):
    cat = hoverData['points'][0]['x']  # 获取鼠标悬停的商品种类

    category_gender_amount = []

    for gen in genders:
        category_gender_amount.append(
            len(df[(df['Product_Category_1'] == cat) & (df['Gender'] == gen)]) +
            len(df[(df['Product_Category_2'] == cat) & (df['Gender'] == gen)]) +
            len(df[(df['Product_Category_3'] == cat) & (df['Gender'] == gen)])
        )

    category_gender_amount_fr = pd.DataFrame({
        'Gender': genders,
        'Amount': category_gender_amount
    })

    fig = px.pie(category_gender_amount_fr, names='Gender', values='Amount',
                 color_discrete_sequence=["#6B81A3", "#CEE5EE", "#D0F0EE", "#97CBE7", "#9AEEDD"],
                 color='Gender',
                 title=f'Gender Proportion for Category {cat} :')

    fig.update_layout(title_font=dict(size=20))

    return fig


@app.callback(
    dependencies.Output('category_city-pie', 'figure'),
    dependencies.Input('amount-category', 'hoverData')
)
def update_category_city_pie(hoverData):
    cat = hoverData['points'][0]['x']  # 获取鼠标悬停的商品种类

    category_city_amount = []

    for cit in cities:
        category_city_amount.append(
            len(df[(df['Product_Category_1'] == cat) & (df['City_Category'] == cit)]) +
            len(df[(df['Product_Category_2'] == cat) & (df['City_Category'] == cit)]) +
            len(df[(df['Product_Category_3'] == cat) & (df['City_Category'] == cit)])
        )

    category_city_amount_fr = pd.DataFrame({
        'City_Category': cities,
        'Amount': category_city_amount
    })

    fig = px.pie(category_city_amount_fr, names='City_Category', values='Amount',
                 color_discrete_sequence=["#6B81A3", "#D0F0EE", "#CEE5EE", "#97CBE7", "#9AEEDD"],
                 color='City_Category',
                 title=f'City Proportion for Category {cat} :')

    fig.update_layout(title_font=dict(size=20))

    return fig


@app.callback(
    dependencies.Output('category_age-pie', 'figure'),
    dependencies.Input('amount-category', 'hoverData')
)
def update_category_age_pie(hoverData):
    cat = hoverData['points'][0]['x']  # 获取鼠标悬停的商品种类

    category_age_amount = []

    for age in ages:
        category_age_amount.append(
            len(df[(df['Product_Category_1'] == cat) & (df['Age'] == age)]) +
            len(df[(df['Product_Category_2'] == cat) & (df['Age'] == age)]) +
            len(df[(df['Product_Category_3'] == cat) & (df['Age'] == age)])
        )

    category_age_amount_fr = pd.DataFrame({
        'Age': ages,
        'Amount': category_age_amount
    })

    fig = px.line(category_age_amount_fr, x='Age', y='Amount',
                  color_discrete_sequence=["#6B81A3", "#CEE5EE", "#D0F0EE", "#97CBE7", "#9AEEDD"],
                  title=f'Age Proportion for Category {cat} :')

    fig.update_layout(title_font=dict(size=20))

    return fig


@app.callback(
    dependencies.Output('gender-ratio', 'figure'),
    [
        dependencies.Input('age-ranges', 'value')
    ]
)
# 函数根据选择的年龄段更新性别比例饼图。
def update_gender_ratio(age_range):
    if age_range == 'All':
        dff = df
    else:
        dff = df[df['Age'] == age_range]

    male = len(dff[dff['Gender'] == 'M'])
    female = len(dff[dff['Gender'] == 'F'])

    ratio_data = pd.DataFrame({
        'Gender': ['Male', 'Female'],
        'Number': [male, female]
    })

    fig = px.pie(ratio_data, values='Number', names='Gender',
                 title='Gender Proportion by Age: ' + ('All' if age_range == 'All' else 'Age ' + age_range),
                 color_discrete_sequence=["#CEE5EE", "#6B81A3", "#D0F0EE", "#97CBE7", "#9AEEDD"],
                 color='Gender',
                 hole=.3)

    fig.update_layout(title_font=dict(size=20))

    return fig


@app.callback(
    dependencies.Output('married-ratio', 'figure'),
    [
        dependencies.Input('age-ranges', 'value')
    ]
)
# 函数根据选择的年龄段更新婚姻状态比例饼图。
def update_married_ratio(age_range):
    if age_range == 'All':
        dff = df
    else:
        dff = df[df['Age'] == age_range]

    married = len(dff[dff['Marital_Status'] == 1])
    unmarried = len(dff[dff['Marital_Status'] == 0])

    ratio_data = pd.DataFrame({
        'Marital_Status': ['Married', 'Unmarried'],
        'Number': [married, unmarried]
    })

    fig = px.pie(ratio_data, values='Number', names='Marital_Status',
                 title='Marital_Status Proportion by Age: ' + ('All' if age_range == 'All' else 'Age ' + age_range),
                 color_discrete_sequence=["#CEE5EE", "#6B81A3", "#D0F0EE", "#97CBE7", "#9AEEDD"],
                 color='Marital_Status',
                 hole=.3)

    fig.update_layout(title_font=dict(size=20))

    return fig


@app.callback(
    dependencies.Output('age-ratio', 'figure'),
    [
        dependencies.Input('genders', 'value'),
        dependencies.Input('city-ratio', 'value')
    ]
)
# 函数根据选择的性别更新年龄比例饼图。
def update_age_ratio(gender, city):
    if gender == 'All' and city == 'All':
        dff = df
    elif gender == 'All':
        dff = df[df['City_Category'] == city[0]]
    elif city == 'All':
        dff = df[df['Gender'] == gender[0]]
    else:
        dff = df[(df['City_Category'] == city[0]) & (df['Gender'] == gender[0])]

    res = []
    for age in ages:
        res.append(len(dff[dff['Age'] == age]))

    ratio_data = pd.DataFrame({
        'Age': ages,
        'Number': res
    })

    fig = px.pie(ratio_data, values='Number', names='Age',
                 title='Age Proportion by Gender and City_Category: ' + gender + ' ; ' + city,
                 color_discrete_sequence=["#CEE5EE", "#6B81A3", "#D0F0EE", "#9AEEDD", "#97CBE7", "#80B4DB", "#74add8"],
                 color='Age',
                 hole=.3)

    fig.update_layout(title_font=dict(size=20))

    return fig


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')