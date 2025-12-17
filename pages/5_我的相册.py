import streamlit as st

st.set_page_config(page_title="相册",page_icon="📷")
st.title("我的相册")

if 'ind' not in st.session_state:
	st.session_state['ind']=0

images=[
    {'url':"http://www.005.tv/uploads/compress/allimg/161215/135J0J47-0.jpg",
     'text':'疯狂动物城'
},{'url':"https://puui.qpic.cn/vpic_cover/n0840zhe16v/n0840zhe16v_hz.jpg/1280",
    'text':'疯狂动物城'
},{'url':"https://pic4.zhimg.com/v2-d31c20b0808136cb6fba690b4f099606_r.jpg?source=1940ef5c",
    'text':'蜡笔小新'
}]

st.image(images[st.session_state['ind']]['url'],
	caption=images[st.session_state['ind']]['text'])

def nextImg():
	st.session_state['ind']=(st.session_state['ind']+1) % len(images)
def prevImg():
	st.session_state['ind']=(st.session_state['ind']-1) % len(images)

c1,c2=st.columns(2)

with c1:
    st.button('上一张',on_click=nextImg)
with c2:
    st.button('下一张',on_click=prevImg)