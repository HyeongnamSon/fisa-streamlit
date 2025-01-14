import streamlit as st 

import pandas as pd
import numpy as np


df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)


st.write("Most objects") # df, err, func, keras!
st.write(["st", "is <", 3])
# st.write_stream(my_generator)
# st.write_stream(my_llm_stream)

st.text("Fixed width text")
st.markdown("# 제목")
st.latex(r""" e^{i\pi} + 1 = 0 """)
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")
st.html("<b>Hi!</b>")


st.dataframe(df)
st.table(df.iloc[0:10])
st.json({"foo":"bar","fu":"ba"})
st.metric("My metric", 42, 2)



st.image("https://i.imgur.com/t2ewhfH.png")
# st.audio(data)
# st.video(data)
# st.video(data, subtitles="./subs.vtt")
st.logo("https://i.imgur.com/t2ewhfH.png")


st.dataframe(df)
st.area_chart(df)
st.bar_chart(df)
st.bar_chart(df, horizontal=True)
st.line_chart(df)
# st.map(df)
st.scatter_chart(df)

# st.altair_chart(chart)
# st.bokeh_chart(fig)
# st.graphviz_chart(fig)
# st.plotly_chart(fig)
# st.pydeck_chart(chart)
# st.pyplot(fig)
# st.vega_lite_chart(df, spec)

# Work with user selections
# event = st.plotly_chart(
#     df,
#     on_select="rerun"
# )
# event = st.altair_chart(
#     chart,
#     on_select="rerun"
# )
# event = st.vega_lite_chart(
#     df,
#     spec,
#     on_select="rerun"
# )
