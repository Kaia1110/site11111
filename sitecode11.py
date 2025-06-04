import streamlit as st
from PIL import Image
import base64
import os

# 配置页面
st.set_page_config(
    page_title="许世晨个人简历",
    layout="wide",
    page_icon="📄"
)

# 定义简历信息
class Resume:
    def __init__(self):
        self.name = "许世晨"
        self.contact = {
            "电话": "13668802266",
            "邮箱": "xushichen2024@163.com",
            "政治面貌": "中共党员"
        }
        self.education = [
            {
                "学校": "香港中文大学",
                "时间": "2024年08月 - 2025年07月",
                "专业": "市场营销专业 硕士",
                "学院": "商学院",
                "地点": "香港",
                "课程": "主要课程:数字营销,大数据策略,社交媒体分析,消费者行为研究,市场研究"
            },
            {
                "学校": "中山大学",
                "时间": "2020年09月 - 2024年06月",
                "专业": "英语语言文学 本科",
                "学院": "外国语学院",
                "地点": "广州",
                "gpa": "GPA:3.9/4.0",
                "论文": "优秀毕业论文(视觉语法视域下国家形象宣传片多模态话语分析)"
            },
            {
                "学校": "伦敦政治经济学院暑校",
                "时间": "2023年07月",
                "专业": "消费者行为研究",
                "成绩": "成绩: A",
                "地点": "伦敦"
            }
        ]
        self.experience = [
            {
                "公司": "realme真我手机",
                "时间": "2025年02月 - 至今",
                "职位": "品牌策划实习生",
                "描述": [
                    "深度分析50+联名案例,覆盖电影和游戏主题,搭建资源池并提炼核心创意,输出案例分析报告3份,为项目提供创新思路和数据支持",
                    "主导撰写联名活动brief初稿,完成英文IMC提案,推动项目通过IP公司审核",
                    "跟进联名项目全流程,与产品线､项目管理､设计部多线程协作,协调跨部门资源,保证项目准时交付"
                ]
            },
            {
                "公司": "山东大学MBA/EMBA教育中心",
                "时间": "2024年05月 - 2024年07月",
                "职位": "国际交流实习生",
                "描述": [
                    "负责国际合作交流项目申报,开拓与成均馆大学管理学教授交流项目,拓展国际学术合作网络,提升单位国际影响力",
                    "协助完成2024年MBA毕业典礼及晚会的策划与执行,保证千人活动顺利执行",
                    "负责国际交流的外文文本起草与翻译,协助国际交流活动的翻译工作"
                ]
            },
            {
                "公司": "国金证券股份有限公司",
                "时间": "2023年07月 - 2023年09月",
                "职位": "投行部实习生",
                "描述": [
                    "对教育信息化领域的企业进行研究,归纳整理同行业可比公司的财务情况,并对各公司应收账款,解释净利润持续下滑的原因及合理性",
                    "协助完成财务调查,包括财务报表数据核对､销售循环的穿行测试｡协助完成销售方的客户访谈,调查其合作､ 采购情况",
                    "参与某激光公司尽职调查阶段,起草尽职调查报告中财务数据部分"
                ]
            },
            {
                "公司": "阿里云研究院",
                "时间": "2021年07月 - 2021年09月",
                "职位": "市场实习生",
                "描述": [
                    "参与市场研究,收集和分析行业数据,探讨云计算行业的竞争格局,包括阿里云､华为云等主要云服务提供商的市场份额和技术优势",
                    "深度参与战略宣传及产品论坛,制作产品论坛宣传视频发布微信视频号,扩大阿里云的行业影响力及知名度",
                    "协助完成线下营销活动的策划与实施,包括产品论坛和达摩院参观活动,邀请潜在客户参与,帮助业务实现更高效的正向用户增长"
                ]
            }
        ]
        self.projects = [
            {
                "名称": "大学生创新创业项目",
                "时间": "2021年04月 - 2022年12月",
                "描述": [
                    "国家级项目:完成国家级项目《多维视角下周边命运共同体的构建研究--以中国对周边国家战略为例》,调研10个周边国家案例,产出 37000字调研报告,项目成果获“优秀”评价",
                    "省级项目:完成省级项目《国际比较视阈下的中国乡村智慧物流发展研究--基于广东省茂名市新塘村脱贫的实际案例考察》,实地考察 基站,拍摄､产出时长20分钟的中､英､日多语纪录片《智运通途》并撰写万字结项论文,项目成果获“优秀”评价"
                ]
            },
            {
                "名称": "2021年中山大学招生直播",
                "时间": "2021年09月 - 2021年10月",
                "描述": [
                    "作为主讲人参与招生办宣传的工作｡在哔哩哔哩､百度､微信视频号等平台进行招生直播,总时长2小时,吸引累计超1万人观看,丰富学 校招生宣传形式"
                ]
            },
            {
                "名称": "第五届全国高校大学生微电影展示活动",
                "时间": "2021年06月",
                "描述": [
                    "独立撰写拍摄脚本与思政讲稿,主导剪辑流程,作品覆盖5000+观众"
                ]
            }
        ]
        self.skills = {
            "办公软件": "熟练使用office办公软件､剪映､Adobe InDesign､Photoshop",
            "数据分析": "Python､R､网络数据抓取､数据可视化",
            "语言能力": "英语流利(专八优秀､雅思7.5)､粤语(日常交流)､西班牙语(初学者)"
        }

# 加载CSS样式
def load_css():
    css = """
    <style>
    .container {
        display: flex;
        flex-wrap: wrap;
        gap: 2rem;
        padding: 2rem;
    }
    .section {
        flex-basis: 100%;
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2rem;
    }
    .contact-info {
        display: flex;
        gap: 2rem;
        margin-bottom: 1rem;
    }
    .experience-item, .project-item {
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #e0e0e0;
    }
    .skill-list {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
    }
    .skill-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 4px;
    }
    @media (max-width: 768px) {
        .container {
            padding: 1rem;
        }
        .skill-list {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# 主函数
def main():
    load_css()
    resume = Resume()
    
    # 头部信息
    with st.container():
        col1, col2 = st.columns([2, 1], gap="large")
        with col1:
            st.title(resume.name)
            st.markdown(f"**政治面貌:** {resume.contact['政治面貌']}", unsafe_allow_html=True)
            
            # 联系信息
            st.markdown("<div class='contact-info'>", unsafe_allow_html=True)
            st.markdown(f"<strong>电话:</strong> {resume.contact['电话']}", unsafe_allow_html=True)
            st.markdown(f"<strong>邮箱:</strong> <a href='mailto:{resume.contact['邮箱']}'>{resume.contact['邮箱']}</a>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # 添加简历下载功能
            try:
                with open("xsc_CV.pdf", "rb") as f:
                    pdf_bytes = f.read()
                st.download_button(
                    "📥 下载PDF简历",
                    pdf_bytes,
                    "许世晨简历.pdf",
                    "application/pdf",
                    key="pdf_download"
                )
            except FileNotFoundError:
                st.warning("未找到PDF简历文件，请将简历保存为'许世晨简历（腾讯IEG）.pdf'并放在同目录下")
        
        with col2:
            # 添加个人照片（需将photo.jpg放在同目录下）
            try:
                st.image("imagexu.jpg", width=200, caption="许世晨", use_column_width=True)
            except FileNotFoundError:
                st.warning("未找到个人照片文件，请将照片保存为photo.jpg并放在同目录下")

    # 教育背景
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader("教育经历")
    for edu in resume.education:
        st.markdown(f"""
        **{edu['学校']}**  
        *{edu['时间']}*  
        {edu['专业']} | {edu.get('学院', '未知学院')} ({edu['地点']})  
        {edu.get('gpa', '')}  
        {edu.get('论文', '')}  
        {edu.get('课程', '')}  
        """)
        st.markdown("---", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 实习经历
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader("实习经历")
    for exp in resume.experience:
        with st.container():
            st.markdown(f"""
            **{exp['职位']}** | {exp['公司']}  
            *{exp['时间']}*  
            """)
            for desc in exp['描述']:
                st.markdown(f"- {desc}")
            st.markdown("---", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 项目经历
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader("项目经历")
    for proj in resume.projects:
        with st.container():
            st.markdown(f"""
            **{proj['名称']}**  
            *{proj['时间']}*  
            """)
            for desc in proj['描述']:
                st.markdown(f"- {desc}")
            st.markdown("---", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 技能与证书
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader("技能/证书及其他")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='skill-card'>", unsafe_allow_html=True)
        st.markdown("<h4>办公软件与工具</h4>")
        st.markdown(resume.skills['办公软件'])
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='skill-card'>", unsafe_allow_html=True)
        st.markdown("<h4>数据分析能力</h4>")
        st.markdown(resume.skills['数据分析'])
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='skill-card'>", unsafe_allow_html=True)
    st.markdown("<h4>语言能力</h4>")
    st.markdown(resume.skills['语言能力'])
    st.markdown("</div>", unsafe_allow_html=True)

    # 页脚
    st.markdown("""
    <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e0e0e0; text-align: center;">
        © 2025 许世晨 | 简历最后更新：2025年06月
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()