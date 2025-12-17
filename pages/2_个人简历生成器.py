import streamlit as st

# 页面配置
st.set_page_config(
    page_title="个人简历生成器",
    page_icon="🔀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 页面标题
st.title("个人简历生成器")

# 分栏：左（表单）、右（预览）
c1,c2 = st.columns([1,2])


# ---------------------- 左侧：个人信息表单 ----------------------
with c1:
    st.subheader("个人信息表单")
    
    # 1. 个人基本信息
    st.markdown("### 基本信息")
    name = st.text_input("姓名")
    gender = st.radio("性别", ["男", "女", "其他"], horizontal=True)
    phone = st.text_input("电话")
    email = st.text_input("邮箱")
    address = st.text_input("地址")
    birth_date = st.date_input("出生日期")
    connect_time= st.selectbox(
          "最佳联系时间", 
          ["8:30","9:30", "10:30","10:30","11:30", "14:30","15:30","16:30", "17:30"]
    )

    st.divider()

    # 2. 求职信息
    st.markdown("### 求职信息")
    job_intention = st.text_input("求职意向")
    job_status = st.selectbox(
        "求职状态", 
        ["在职-考虑机会", "离职-随时到岗", "在校-寻找实习"]
    )
    salary = st.slider(
        "期望薪资（元）", 
        min_value=3000, max_value=20000, 
        value=(5000, 8000)
    )
    st.divider()

    # 3. 教育背景
    st.markdown("### 教育背景")
    education = st.selectbox(
        "学历", 
        ["本科", "大专", "硕士", "博士", "其他"]
    )
    major = st.text_input("专业")
    st.divider()

    # 4. 技能与经验
    st.markdown("### 技能与经验")
    languages= st.multiselect(
        "语言能力", 
        ["中文", "英语", "法语", "日语", "德语", "西班牙语", "韩语"]
    )
    skills = st.multiselect(
        "专业技能", 
        ["HTML/CSS", "Java", "Python", "JavaScript", "SQL", "数据分析", "机器学习", "项目管理", "UI设计"]
    )
    work_exp = st.slider(
        "工作经验（年）", 
        min_value=0, max_value=10, 
        value=0
    )
    st.divider()

    # 5. 个人简介
    st.markdown("### 个人简介")
    intro = st.text_area("简介内容", height=150)
    st.divider()

    # 6. 头像上传
    st.markdown("### 头像上传")
    avatar = st.file_uploader("支持JPG/PNG格式", type=["jpg", "jpeg", "png"])


# ---------------------- 右侧：简历实时预览 ----------------------
with c2:
    st.header("简历实时预览")
    
    # 姓名（带下划线）
    st.markdown(
        f"<h3 style='border-bottom: 2px solid #1E90FF; padding-bottom: 8px;'>{name if name else '请输入姓名'}</h3>",
        unsafe_allow_html=True
    )

    # 头像 + 基础信息栏
    preview_top = st.columns([4, 6])
    with preview_top[0]:
        # 显示头像
        if avatar:
            st.image(avatar, width=200)
        else:
            st.image("https://via.placeholder.com/100", width=100)
    
    with preview_top[1]:
        st.write(f"⚧性别：{gender}")
        st.write(f"📜学历：{education}")
        st.write(f"➡求职意向：{job_intention}")
        st.write(f"🥰期望薪资：{salary[0]} - {salary[1]}元")
        st.write(f"🚩求职状态：{job_status}")
        st.write(f"📞最佳联系时间： {connect_time}")
        st.write(f"☎电话：{phone}")
        st.write(f"📮邮箱：{email}")
        st.write(f"🐣出生日期：{birth_date}")

    # 个人简介
    st.subheader("🗂个人简介")
    st.write(intro if intro else "请输入个人简介内容")
    st.divider()

    preview_top = st.columns([1,1,1])
with preview_top[0]:
    # 专业技能
    st.subheader("🔍 专业技能")
    if skills:
        for skill in skills:
            st.write(f"- {skill}")
    else:
        st.write("请选择你的专业技能")
    st.divider()
with preview_top[1]:
    st.subheader("🗨语言能力")
    if languages:
        for language in languages:
            st.write(f"- {language}")
    else:
        st.write("请选择你会的语言")
    st.divider()
with preview_top[2]:
    # 工作经验
    st.subheader("❤工作经验")
    st.write(f"{work_exp} 年")
    st.divider()