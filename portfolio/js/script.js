document.addEventListener('DOMContentLoaded', () => {

  const followCursor = () => {
    const el = document.querySelector('.backgrount-lighted');
    window.addEventListener('mousemove', e => {
      const target = e.target;
      if (!target) return;
      el.style.left = e.pageX + 'px'
      el.style.top = e.pageY + 'px'
    })
  }

  followCursor()
})
let resolution = 2000;
for (let counter = 0; counter < resolution; counter++) {
  let pixel = document.createElement("div");
  if (counter % 2)
    pixel.classList = "rhombus rhombus-offset"
  else
    pixel.classList = "rhombus"
  document.querySelector(".slider-intro-background").appendChild(pixel);
}
//  progress
progressContent = document.querySelector(".skills-content");
addSkill("HTML", 90, progressContent);
addSkill("CSS", 95, progressContent);
addSkill("JS", 80, progressContent);
addSkill("PYTHON", 95, progressContent);
addSkill("FLASK", 70, progressContent);
addSkill("MICROSOFT ACCESS", 80, progressContent);
addSkill("SQL", 50, progressContent);
addSkill("JAVA", 60, progressContent);
addSkill("C", 50, progressContent);
addSkill("React", 20, progressContent);


function addSkill(skill, level, element) {
  let bar_cont = document.createElement("div");
  bar_cont.classList.add('bar-container');
  let bar = document.createElement("div");
  bar.classList.add('progress');
  p = skill + "<span>"+ level + "%</span>";
  bar.innerHTML = p;
  bar.style = ("width: " + level + "%")
  bar_cont.appendChild(bar)
  progressContent.appendChild(bar_cont);
}