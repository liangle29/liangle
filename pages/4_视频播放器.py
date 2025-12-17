# 导入streamlit库并简写为st，streamlit是用于快速构建Web应用的Python库
import streamlit as st

# 设置页面配置：页面标题为“番剧世界”，页面图标为星星⭐
st.set_page_config(page_title="番剧世界",page_icon="⭐")

# 定义视频数据数组，包含3个剧集的URL、标题、集数信息
video_arr=[
    {
    'url':'https://video.dispatch.tc.qq.com/B_fXrb0otmtGHxqhZ5HYDTdgGqKjU9JAAVQvkYJ-wQ8fb906n7kSBfIFfUWSI8L1jd6wyaEfeylD8-UkJPiJbhtX4UY2huR7lIs9OX_gjCz6019rb6ZA47pLsE1EwuiT1jjlaCB4OFmik13QiD1PJimA/svp_50112/gzc_1000102_0b533abncaac54aaw54m2nr4fwgd2hjqfvka.f2.mp4?vkey=B70F4A79BA2B4A291F537D7821A373D438680090A6ABC3A246B154DF1E7A311BC1F28C3601952C3923121E73B59D4A159AC1176072F1369C7962A1A63215C95994D5F863C60DFFCDF06424C0727D38860BF4F2AB7C650D5A4039CADFE95B9C097E3DEE750DD9056647EEBE2F225DD2356C8503AD2895768909D854C9338A3CF838AEB72AA367AA6519DFE6BF36EA74F8E533DF2F7CCA08E0',  # 第1集视频地址
    'title':'第1集',  # 第1集标题
    'episode':1  # 第1集集数标识
    },{
    'url':'https://www.w3schools.com/html/movie.mp4',  # 第2集视频地址
    'title':'第2集',  # 第2集标题
    'episode':2  # 第2集集数标识
    },{
    'url':'https://media.w3.org/2010/05/sintel/trailer.mp4',  # 第3集视频地址
    'title':'第3集',  # 第3集标题
    'episode':3  # 第3集集数标识
    }]

# 初始化session_state：如果'ind'键不存在，设置初始值为0（默认选中第1集）
# session_state用于在Streamlit应用中保存跨交互的状态
if 'ind' not in st.session_state:
    st.session_state['ind']=0

# 获取当前选中剧集的集数：根据session_state中的'ind'索引，从video_arr中取对应episode值
current_episode = video_arr[st.session_state['ind']]["episode"]

# 设置页面标题：拼接“开心超人 第X集”，X为当前选中的集数
st.title(f"开心超人 第{current_episode}集")

# 播放当前选中剧集的视频：根据'ind'索引取对应URL，设置自动播放
st.video(video_arr[st.session_state['ind']]['url'],autoplay=True)

# 定义剧集切换函数：接收索引i，更新session_state中的'ind'为选中的索引
def play(i):
        st.session_state['ind']=int(i)

# --- 用columns将按钮排成一排 ---
# 创建与剧集数量相同的列容器（3列），用于横向排列按钮
cols = st.columns(len(video_arr))  
# 遍历剧集索引，为每个剧集创建按钮
for i in range(len(video_arr)):
    with cols[i]:  # 将按钮放入对应的列中，实现横向排列
        # 创建剧集按钮：显示“第X集”，宽度适配列容器，点击时调用play函数并传入当前索引i
        st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))

# 添加分隔线：用于视觉上分隔视频/按钮区域和简介区域
st.markdown('***')

# 添加“简介”小标题（6级标题）
st.markdown('###### 简介')

# 显示番剧简介文本
st.text("五超人在执行任务中，意外发现体内暗藏了能控制他们的程序代码，在调查过程中，超人们发现所有的线索都指向了宇宙开发集团-五金公司。超人们为了解开谜题，踏上了寻找真相之路，五金公司的阴谋也逐渐浮出水面。原来，五金公司曾经拥有过诞生超人们的超能机械石，并试图将超人改造成为自己的武器，从而称霸宇宙。超人们得知真相后，合力摧毁了五金公司，解决了宇宙的危机。")

# 添加“配音”小标题（6级标题）（此处未补充配音内容，仅创建标题）
st.markdown('###### 配音')
st.text("开心超人：刘红韵 甜心超人：邓玉婷 花心超人：严彦子 粗心超人：祖晴")
