from pptx import Presentation1
from pptx.util import Inches

# Create a PowerPoint presentation object
prs = Presentation()

# Title Slide
slide_layout = prs.slide_layouts[0]  # 0 - Title Slide
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "Contributions of Indian Mathematicians and Statisticians"
subtitle.text = "A Journey Through History\nYour Name\nDate"

# Introduction Slide
slide_layout = prs.slide_layouts[1]  # 1 - Title and Content
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
content = slide.placeholders[1]
title.text = "Introduction"
content.text = ("India has a rich heritage of mathematics and statistics, with contributions that span millennia and have significantly influenced the global understanding of these fields. "
                "From ancient scholars who laid the foundational concepts in mathematics to modern pioneers who advanced statistical theories and applications, Indian thinkers have played a crucial role in the development of mathematical and statistical sciences.")

# Function to add a slide for a mathematician/statistician
def add_person_slide(title_text, name, contributions, works):
    slide_layout = prs.slide_layouts[1]  # 1 - Title and Content
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    title.text = title_text
    content.text = (f"**Name:** {name}\n\n"
                    f"**Contributions:** {contributions}\n\n"
                    f"**Major Works:** {works}")

# Adding slides for mathematicians
add_person_slide("Indian Mathematicians", "Aryabhata (476-550)", 
                 "Aryabhata was one of the first major mathematicians and astronomers from the classical age of Indian mathematics and Indian astronomy. He introduced the concept of zero, approximated the value of π (pi) to four decimal places, and developed the place value system. He also worked on the approximation of sine tables and contributed significantly to trigonometry.", 
                 "Aryabhatiya and Arya-siddhanta")

add_person_slide("Indian Mathematicians", "Brahmagupta (598-668)", 
                 "Brahmagupta made significant contributions to mathematics and astronomy. He provided explicit rules for arithmetic operations involving zero, formulated the concept of negative numbers, and solved quadratic equations. His work included important rules for calculating the area of cyclic quadrilaterals and the length of diagonals.", 
                 "Brahmasphutasiddhanta")

add_person_slide("Indian Mathematicians", "Bhaskara II (1114-1185)", 
                 "Also known as Bhaskaracharya, he made groundbreaking advances in algebra, arithmetic, geometry, and trigonometry. He is famous for his work on calculus, including the concepts of differentiation and integration. His work in astronomy and mathematics laid the foundation for later developments in these fields.", 
                 "Siddhanta Shiromani, which includes books like Lilavati and Bijaganita")

add_person_slide("Indian Mathematicians", "Srinivasa Ramanujan (1887-1920)", 
                 "Ramanujan was a self-taught mathematician who made substantial contributions to mathematical analysis, number theory, infinite series, and continued fractions. He compiled nearly 3,900 results, including many innovative discoveries, despite having no formal training in mathematics.", 
                 "Notebooks containing his theorems, which have inspired and advanced many areas of mathematics")

add_person_slide("Indian Mathematicians", "Harish-Chandra (1923-1983)", 
                 "Harish-Chandra was a mathematician who specialized in representation theory and harmonic analysis on Lie groups. His work has had a profound impact on the field of mathematics, particularly in the areas of quantum mechanics and the theory of group representations.", 
                 "Contributions to the mathematical formulation of quantum mechanics and representation theory")

# Adding slides for statisticians
add_person_slide("Indian Statisticians", "Rao Bahadur K. S. Krishnan (1898-1961)", 
                 "Krishnan was a pioneering Indian physicist and statistician known for his work on X-ray diffraction and collaborations with Nobel laureate C.V. Raman. His contributions to statistics include significant advancements in statistical mechanics and theoretical physics.", 
                 "Studies in X-ray diffraction and statistical mechanics")

add_person_slide("Indian Statisticians", "P.C. Mahalanobis (1893-1972)", 
                 "Mahalanobis is best known for introducing the Mahalanobis distance, a measure used in multivariate analysis. He pioneered large-scale sample surveys in India and established the Indian Statistical Institute. His work laid the foundation for modern statistics and its applications in various fields.", 
                 "Mahalanobis distance, large-scale sample survey methodologies")

add_person_slide("Indian Statisticians", "C.R. Rao (1920-2020)", 
                 "Rao made significant contributions to statistics, including the development of the Cramer-Rao bound and the Rao-Blackwell theorem. His work in multivariate analysis and statistical inference has been foundational to the field. He also contributed to the theory of estimation and hypothesis testing.", 
                 "Contributions to statistical theory and inference, multivariate analysis")

add_person_slide("Indian Statisticians", "S.R. Srinivasa Varadhan (1940-)", 
                 "Varadhan is renowned for his work in probability theory, particularly in the field of large deviations. His contributions have profoundly influenced the study of stochastic processes, statistical mechanics, and random matrices. He received the Abel Prize in 2007 for his work.", 
                 "Large deviations theory, contributions to probability and stochastic processes")

add_person_slide("Indian Statisticians", "Raghunathan S. (1941-)", 
                 "Raghunathan is a distinguished mathematician known for his work in ergodic theory, Lie groups, and discrete subgroups. His research has been instrumental in the development of modern mathematical theory and has influenced a wide range of mathematical disciplines.", 
                 "Contributions to ergodic theory and Lie groups")

# Vedic Mathematics Slide
add_person_slide("Vedic Mathematics", "Bharati Krishna Tirthaji (1884-1960)", 
                 "Bharati Krishna Tirthaji is credited with the rediscovery of Vedic mathematics, which he claimed to have reconstructed from ancient Indian scriptures called the Vedas. His work consists of a set of techniques for solving mathematical problems quickly and efficiently, which he detailed in his book 'Vedic Mathematics.'", 
                 "Vedic Mathematics, techniques for quick mental calculations")

# Conclusion Slide
slide_layout = prs.slide_layouts[1]  # 1 - Title and Content
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
content = slide.placeholders[1]
title.text = "Conclusion"
content.text = ("This presentation has highlighted the remarkable contributions of Indian mathematicians and statisticians throughout history. "
                "From ancient scholars who laid the groundwork for modern mathematics to contemporary pioneers who advanced statistical methods, their work has had a lasting impact on these fields. "
                "The enduring legacy of these brilliant minds continues to inspire and influence the world of mathematics and statistics today.")

# Save the presentation
prs.save("Indian_Mathematicians_and_Statisticians_Presentation.pptx")
