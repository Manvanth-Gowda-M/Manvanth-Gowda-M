<div align="center">

<!-- ✨ Modern Animated Hero Section ✨ -->
<div style="position: relative; padding: 40px 20px; background: linear-gradient(135deg, #0d1117 0%, #161b22 50%, #21262d 100%); border-radius: 20px; margin-bottom: 30px; overflow: hidden; border: 2px solid #58A6FF; box-shadow: 0 20px 40px rgba(88, 166, 255, 0.3);">

  <!-- Floating Background Elements -->
  <div style="position: absolute; top: 20px; left: 20px; animation: float 6s ease-in-out infinite; opacity: 0.6;">
    <div style="width: 40px; height: 40px; background: linear-gradient(45deg, #58A6FF, #3fb950); border-radius: 50%; filter: blur(2px);"></div>
  </div>
  <div style="position: absolute; top: 60px; right: 30px; animation: float 4s ease-in-out infinite reverse; opacity: 0.4;">
    <div style="width: 25px; height: 25px; background: linear-gradient(45deg, #bf4b8a, #f7931e); border-radius: 50%; filter: blur(1px);"></div>
  </div>
  <div style="position: absolute; bottom: 30px; left: 40px; animation: float 5s ease-in-out infinite; opacity: 0.5;">
    <div style="width: 30px; height: 30px; background: linear-gradient(45deg, #f85149, #58A6FF); border-radius: 50%; filter: blur(2px);"></div>
  </div>

  <!-- Main Content -->
  <div style="position: relative; z-index: 2;">
    
    <!-- Animated Greeting -->
    <div style="animation: slideInFromTop 1s ease-out;">
      <h1 style="color: #58A6FF; font-size: 2.5em; margin: 0 0 10px 0; font-weight: 300; text-shadow: 0 0 20px rgba(88, 166, 255, 0.5);">
        Hi there! 👋
      </h1>
    </div>

    <!-- Animated Name with Gradient Effect -->
    <div style="animation: slideInFromBottom 1.2s ease-out; animation-delay: 0.3s; animation-fill-mode: both;">
      <h2 style="
        font-size: 3.5em; 
        margin: 0; 
        font-weight: 700;
        background: linear-gradient(-45deg, #58A6FF, #3fb950, #bf4b8a, #f7931e, #58A6FF);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientShift 3s ease-in-out infinite, pulse 2s ease-in-out infinite alternate;
        text-shadow: 0 0 30px rgba(88, 166, 255, 0.3);
        filter: drop-shadow(0 0 10px rgba(88, 166, 255, 0.2));
      ">
        Manvanth Gowda M
      </h2>
    </div>

    <!-- Animated Subtitle -->
    <div style="animation: fadeInScale 1.5s ease-out; animation-delay: 0.6s; animation-fill-mode: both;">
      <h3 style="
        color: #c9d1d9; 
        font-size: 1.8em; 
        margin: 15px 0 20px 0; 
        font-weight: 400;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
        animation: glow 2s ease-in-out infinite alternate;
      ">
        🎓 Computer Science Engineer
      </h3>
    </div>

    <!-- Animated Description -->
    <div style="animation: fadeInScale 1.8s ease-out; animation-delay: 0.9s; animation-fill-mode: both;">
      <p style="
        color: #8b949e; 
        font-size: 1.3em; 
        margin: 0 0 25px 0; 
        font-weight: 300;
        line-height: 1.6;
        max-width: 600px;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
      ">
        🚀 AI & Full-Stack Developer crafting intelligent solutions and innovative experiences
      </p>
    </div>

    <!-- Animated Tech Stack Pills -->
    <div style="animation: slideInFromRight 2s ease-out; animation-delay: 1.2s; animation-fill-mode: both; display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; margin-bottom: 25px;">
      <span style="
        background: linear-gradient(135deg, #58A6FF, #3fb950); 
        color: white; 
        padding: 8px 16px; 
        border-radius: 25px; 
        font-size: 0.9em; 
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(88, 166, 255, 0.3);
        animation: float 3s ease-in-out infinite;
        animation-delay: 0s;
      ">🤖 AI/ML</span>
      <span style="
        background: linear-gradient(135deg, #bf4b8a, #f7931e); 
        color: white; 
        padding: 8px 16px; 
        border-radius: 25px; 
        font-size: 0.9em; 
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(191, 75, 138, 0.3);
        animation: float 3s ease-in-out infinite;
        animation-delay: 0.5s;
      ">⚡ Full-Stack</span>
      <span style="
        background: linear-gradient(135deg, #f7931e, #f85149); 
        color: white; 
        padding: 8px 16px; 
        border-radius: 25px; 
        font-size: 0.9em; 
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(247, 147, 30, 0.3);
        animation: float 3s ease-in-out infinite;
        animation-delay: 1s;
      ">🔬 Innovation</span>
    </div>

    <!-- Welcome Message -->
    <div style="animation: fadeInScale 2.2s ease-out; animation-delay: 1.5s; animation-fill-mode: both;">
      <p style="
        color: #58A6FF; 
        font-size: 1.1em; 
        margin: 0; 
        font-weight: 500;
        text-shadow: 0 0 10px rgba(88, 166, 255, 0.3);
      ">
        💡 Passionate about building the future, one line of code at a time
      </p>
    </div>

  </div>
</div>

<!-- CSS Animations -->
<style>
@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

@keyframes pulse {
  0% { transform: scale(1); }
  100% { transform: scale(1.02); }
}

@keyframes glow {
  0% { text-shadow: 0 0 5px rgba(88, 166, 255, 0.5); }
  100% { text-shadow: 0 0 20px rgba(88, 166, 255, 0.8), 0 0 30px rgba(88, 166, 255, 0.3); }
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(180deg); }
}

@keyframes slideInFromTop {
  0% { transform: translateY(-50px); opacity: 0; }
  100% { transform: translateY(0); opacity: 1; }
}

@keyframes slideInFromBottom {
  0% { transform: translateY(50px); opacity: 0; }
  100% { transform: translateY(0); opacity: 1; }
}

@keyframes slideInFromRight {
  0% { transform: translateX(50px); opacity: 0; }
  100% { transform: translateX(0); opacity: 1; }
}

@keyframes fadeInScale {
  0% { transform: scale(0.8); opacity: 0; }
  100% { transform: scale(1); opacity: 1; }
}
</style>

<!-- Enhanced Social Stats Section -->
<div style="display: flex; justify-content: center; align-items: center; gap: 15px; flex-wrap: wrap; margin-bottom: 30px; padding: 0 10px; animation: fadeInScale 2.5s ease-out; animation-delay: 1.8s; animation-fill-mode: both;">
  <span style="margin: 5px; animation: float 4s ease-in-out infinite;">
    <a href="https://github.com/Manvanth-Gowda-M?tab=followers">
      <img src="https://img.shields.io/github/followers/Manvanth-Gowda-M?style=flat-square&color=58A6FF" alt="GitHub Followers" style="box-shadow: 0 4px 15px rgba(88, 166, 255, 0.3); border-radius: 8px;" />
    </a>
  </span>
  <span style="margin: 5px; animation: float 4s ease-in-out infinite; animation-delay: 0.5s;">
    <a href="https://github.com/Manvanth-Gowda-M?tab=repositories">
      <img src="https://img.shields.io/github/stars/Manvanth-Gowda-M/Resmeinfo_project?style=flat-square&color=58A6FF" alt="GitHub Stars" style="box-shadow: 0 4px 15px rgba(88, 166, 255, 0.3); border-radius: 8px;" />
    </a>
  </span>
</div>

</div>

---

## 👨‍💻 About Me

<!-- Mobile-responsive About Section with optimized styling -->
<div align="center" style="animation: fadeIn 1.5s ease-in-out; max-width: 100%; padding: 0 15px;">

<div style="max-width: 800px; margin: 0 auto; padding: 20px; background: linear-gradient(145deg, #0d1117, #161b22); border-radius: 15px; border: 2px solid #58A6FF; box-shadow: 0 10px 30px rgba(88, 166, 255, 0.2);">

<p style="color: #c9d1d9; font-size: 1.1em; line-height: 1.8; text-align: left; margin-bottom: 15px;">
  <span style="color: #58A6FF; font-weight: bold;">🎓</span> I'm a passionate <span style="color: #58A6FF; font-weight: bold;">Computer Science Engineering student</span> with a deep fascination for <span style="color: #3fb950; font-weight: bold;">AI systems</span> and <span style="color: #bf4b8a; font-weight: bold;">open-source development</span>. My journey in technology is driven by curiosity and the desire to create impactful solutions.
</p>

<p style="color: #c9d1d9; font-size: 1.1em; line-height: 1.8; text-align: left; margin-bottom: 15px;">
  <span style="color: #58A6FF; font-weight: bold;">🧠</span> I'm particularly interested in <span style="color: #f7931e; font-weight: bold;">MCP servers</span>, <span style="color: #f7931e; font-weight: bold;">prompt engineering</span>, and building <span style="color: #f7931e; font-weight: bold;">intelligent workflows</span> that enhance productivity and creativity. Currently, I'm diving deep into <span style="color: #3fb950; font-weight: bold;">advanced AI pipelines</span> and <span style="color: #3fb950; font-weight: bold;">full-stack development</span> as part of the <span style="color: #bf4b8a; font-weight: bold;">NextGenX</span> initiative.
</p>

<p style="color: #c9d1d9; font-size: 1.1em; line-height: 1.8; text-align: left; margin-bottom: 15px;">
  <span style="color: #58A6FF; font-weight: bold;">🌱</span> Based in <span style="color: #f7931e; font-weight: bold;">🇮🇳 India</span>, I'm committed to continuous learning and growth. I believe in the power of technology to transform lives and I'm always exploring new ways to leverage <span style="color: #3fb950; font-weight: bold;">cutting-edge AI technologies</span> to solve real-world problems.
</p>

<p style="color: #c9d1d9; font-size: 1.1em; line-height: 1.8; text-align: left; margin-bottom: 0;">
  <span style="color: #58A6FF; font-weight: bold;">🔭</span> When I'm not coding, you can find me experimenting with new technologies, contributing to open-source projects, or exploring the latest advancements in <span style="color: #bf4b8a; font-weight: bold;">machine learning</span> and <span style="color: #bf4b8a; font-weight: bold;">artificial intelligence</span>.
</p>

</div>

</div>

---

---

## 💻 Technology Stack

### 🧠 Programming Languages
<div align="center" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; padding: 0 15px;">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white&style=flat-square)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black&style=flat-square)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white&style=flat-square)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white&style=flat-square)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white&style=flat-square)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white&style=flat-square)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white&style=flat-square)

</div>

### 🎨 Frontend Technologies
<div align="center" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; padding: 0 15px;">

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB&style=flat-square)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white&style=flat-square)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white&style=flat-square)
![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D&style=flat-square)
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white&style=flat-square)

</div>

### ⚙️ Backend & Databases
<div align="center" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; padding: 0 15px;">

![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white&style=flat-square)
![Express.js](https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white&style=flat-square)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white&style=flat-square)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white&style=flat-square)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black&style=flat-square)

</div>

### 🤖 AI & Machine Learning
<div align="center" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; padding: 0 15px;">

![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white&style=flat-square)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white&style=flat-square)
![scikit-learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white&style=flat-square)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white&style=flat-square)

</div>

### 🛠️ Development Tools
<div align="center" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; padding: 0 15px;">

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white&style=flat-square)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white&style=flat-square)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white&style=flat-square)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black&style=flat-square)

</div>

---

## 🌟 Featured Projects

<div align="center" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; padding: 0 15px;">

<!-- Project 1: NutriGuideFLU -->
<div style="display: inline-block; margin: 10px; padding: 25px; border: 2px solid #58A6FF; border-radius: 15px; background: linear-gradient(145deg, #0d1117, #161b22); box-shadow: 0 10px 30px rgba(88, 166, 255, 0.3); transition: all 0.3s ease; max-width: 500px; width: 100%; flex: 1; min-width: 300px;">

<h3 style="color: #58A6FF; margin-bottom: 15px; font-size: 1.5em;">🍎 NutriGuideFLU</h3>

<p style="color: #c9d1d9; margin-bottom: 15px; line-height: 1.6;">
A comprehensive nutrition guidance system powered by AI for personalized meal planning and health optimization.
</p>

<div style="margin-bottom: 15px; display: flex; flex-wrap: wrap; gap: 5px;">
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">Python</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">TensorFlow</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">React</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">Node.js</span>
</div>

<!-- ANIMATED GITHUB BUTTON -->
<a href="https://github.com/NextGenXplorer/NutriGuideFLU" style="text-decoration: none; display: inline-block;">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=20&duration=3000&pause=1000&color=238636&width=250&height=50&center=true&vCenter=true&lines=View+on+GitHub;Check+it+out+🚀;Click+to+Visit" alt="View on GitHub" />
</a>

</div>

<!-- Project 2: Resmeinfo_project -->
<div style="display: inline-block; margin: 10px; padding: 25px; border: 2px solid #58A6FF; border-radius: 15px; background: linear-gradient(145deg, #0d1117, #161b22); box-shadow: 0 10px 30px rgba(88, 166, 255, 0.3); transition: all 0.3s ease; max-width: 500px; width: 100%; flex: 1; min-width: 300px;">

<h3 style="color: #58A6FF; margin-bottom: 15px; font-size: 1.5em;">📋 Resmeinfo_project</h3>

<p style="color: #c9d1d9; margin-bottom: 15px; line-height: 1.6;">
AI-powered resume builder with intelligent optimization for job applications and career advancement.
</p>

<div style="margin-bottom: 15px; display: flex; flex-wrap: wrap; gap: 5px;">
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">React</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">Node.js</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">Express</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">MongoDB</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">OpenAI API</span>
</div>

<!-- ANIMATED GITHUB BUTTON -->
<a href="https://github.com/Manvanth-Gowda-M/Resmeinfo_project" style="text-decoration: none; display: inline-block;">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=20&duration=3000&pause=1000&color=238636&width=250&height=50&center=true&vCenter=true&lines=View+on+GitHub;Check+it+out+🚀;Click+to+Visit" alt="View on GitHub" />
</a>

</div>

<!-- Project 3: Storybook -->
<div style="display: inline-block; margin: 10px; padding: 25px; border: 2px solid #58A6FF; border-radius: 15px; background: linear-gradient(145deg, #0d1117, #161b22); box-shadow: 0 10px 30px rgba(88, 166, 255, 0.3); transition: all 0.3s ease; max-width: 500px; width: 100%; flex: 1; min-width: 300px;">

<h3 style="color: #58A6FF; margin-bottom: 15px; font-size: 1.5em;">📚 Storybook</h3>

<p style="color: #c9d1d9; margin-bottom: 15px; line-height: 1.6;">
Interactive storytelling platform with collaborative features and AI-generated narratives for immersive experiences.
</p>

<div style="margin-bottom: 15px; display: flex; flex-wrap: wrap; gap: 5px;">
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">React</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">TypeScript</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">Tailwind CSS</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">Flask</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">PostgreSQL</span>
</div>

<!-- ANIMATED GITHUB BUTTON -->
<a href="https://github.com/Manvanth-Gowda-M/storybook" style="text-decoration: none; display: inline-block;">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=20&duration=3000&pause=1000&color=238636&width=250&height=50&center=true&vCenter=true&lines=View+on+GitHub;Check+it+out+🚀;Click+to+Visit" alt="View on GitHub" />
</a>

</div>

<!-- Project 4: KannadadKey -->
<div style="display: inline-block; margin: 10px; padding: 25px; border: 2px solid #58A6FF; border-radius: 15px; background: linear-gradient(145deg, #0d1117, #161b22); box-shadow: 0 10px 30px rgba(88, 166, 255, 0.3); transition: all 0.3s ease; max-width: 500px; width: 100%; flex: 1; min-width: 300px;">

<h3 style="color: #58A6FF; margin-bottom: 15px; font-size: 1.5em;">⌨️ KannadadKey</h3>

<p style="color: #c9d1d9; margin-bottom: 15px; line-height: 1.6;">
Kannada language keyboard interface and typing tutor with smart prediction features and NLP capabilities.
</p>

<div style="margin-bottom: 15px; display: flex; flex-wrap: wrap; gap: 5px;">
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">Python</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">PyQt5</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">NLP</span>
<span style="background: #21262d; color: #58A6FF; padding: 5px 10px; border-radius: 15px; font-size: 0.9em;">Machine Learning</span>
</div>

<!-- ANIMATED GITHUB BUTTON -->
<a href="https://github.com/Manvanth-Gowda-M/kannadakeybynxg" style="text-decoration: none; display: inline-block;">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=20&duration=3000&pause=1000&color=238636&width=250&height=50&center=true&vCenter=true&lines=View+on+GitHub;Check+it+out+🚀;Click+to+Visit" alt="View on GitHub" />
</a>

</div>

</div>

---

## 📈 Activity & Achievements

<div align="center" style="padding: 0 10px;">

<!-- GitHub Activity Graph - Mobile Responsive -->
<div style="width: 100%; max-width: 100%; margin-bottom: 20px;">
  <img alt="GitHub Activity Graph" src="https://github-readme-activity-graph.vercel.app/graph?username=Manvanth-Gowda-M&bg_color=0d1117&color=58A6FF&line=3fb950&point=bf4b8a&area=true&area_color=1f6feb33&hide_title=true" style="width: 100%; height: auto;" />
</div>

</div>

---

## 🤝 Let's Connect

<div align="center">

<!-- Social Links with Mobile-Responsive Layout -->
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; padding: 0 15px; max-width: 900px; margin: 0 auto;">

<!-- Email -->
<a href="mailto:appumanu3214@gmail.com" style="text-decoration: none;">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=20&duration=3000&pause=1000&color=EA4335&width=200&height=50&center=true&vCenter=true&lines=Email+Me;Let's+Talk+📧" alt="Email" />
</a>

<!-- LinkedIn -->
<a href="https://www.linkedin.com/in/manvanth-gowda-m-50288039b" style="text-decoration: none;">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=20&duration=3000&pause=1000&color=0077B5&width=200&height=50&center=true&vCenter=true&lines=LinkedIn;Connect+🤝" alt="LinkedIn" />
</a>

<!-- Instagram -->
<a href="https://www.instagram.com/appu_kannadigaa" style="text-decoration: none;">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=20&duration=3000&pause=1000&color=E4405F&width=200&height=50&center=true&vCenter=true&lines=Instagram;Follow+📸" alt="Instagram" />
</a>

<!-- Portfolio -->
<a href="https://manvanth.vercel.app/" style="text-decoration: none;">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=20&duration=3000&pause=1000&color=7B68EE&width=200&height=50&center=true&vCenter=true&lines=Portfolio;My+Work+🌐" alt="Portfolio" />
</a>

</div>

</div>

---

## 🚀 Current Focus & Learning

<div align="center">

### 🔬 What I'm Currently Working On:
- 🏗️ Building intelligent AI pipelines for NextGenX projects
- 📈 Improving AI model performance for real-world applications  
- 🔬 Researching advanced prompt engineering techniques
- 🌐 Exploring new web technologies for enhanced user experiences

### 🎯 Areas I'm Excited About:
- 🤖 Advanced Deep Learning architectures
- 🎯 Production-level AI deployment
- 🔄 Microservices architecture
- 📊 Data visualization and analytics
- 🧠 MCP (Model Context Protocol) server development

</div>

---

## 🎯 Open to Collaborations

<div align="center">

I'm always excited to work on innovative projects, especially in:

**🤖 AI/ML Development** • **🌐 Full-Stack Applications** • **🔧 MCP Server Development** • **⚡ Prompt Engineering** • **💡 Open Source Projects**

**Feel free to reach out if you have an interesting project or collaboration opportunity!** 🤝

</div>

---

## 📊 Visitor Statistics

<div align="center" style="padding: 0 15px;">

<p><strong>Thanks for visiting my profile! 🚀</strong></p>

<div style="max-width: 300px; margin: 0 auto;">
  <img alt="Visitor Counter" src="https://profile-counter.glitch.me/Manvanth-Gowda-M/count.svg" style="width: 100%; height: auto;" />
</div>

</div>

---

<div align="center" style="padding: 0 15px;">

### 🔔 Connect With Me

<p><strong>I'm always excited to discuss new ideas and opportunities!</strong></p>

<!-- Final Call-to-Action Button -->
<a href="https://www.linkedin.com/in/manvanth-gowda-m-50288039b" style="text-decoration: none;">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=20&duration=3000&pause=1000&color=0077B5&width=350&height=60&center=true&vCenter=true&lines=💼+Let's+Connect+on+LinkedIn" alt="LinkedIn Connect" />
</a>

</div>

---

<div align="center" style="padding: 0 15px;">

<p><sub>🚀 Built with ❤️ and lots of ☕ by Manvanth Gowda M</sub></p>
<p><sub>🕒 Last Updated: December 2024</sub></p>

</div>