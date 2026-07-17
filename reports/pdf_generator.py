import os
import re
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

from reportlab.lib.styles import ParagraphStyle


def create_pdf(report_text, filename, dataset_name="Unknown Dataset"):

    os.makedirs("reports", exist_ok=True)

    pdf_path = os.path.join("reports", filename)

    doc = SimpleDocTemplate(
        pdf_path,
        rightMargin=40,
        leftMargin=40,
        topMargin=50,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title = ParagraphStyle(
        "NovaTitle",
        parent=styles["Title"],
        fontSize=24,
        spaceAfter=6
    )
    heading = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=15,
        spaceBefore=10,
        spaceAfter=10
    )
    normal = styles["BodyText"]

    story = []

    # Title

    story.append(Paragraph("EXECUTIVE BUSINESS REPORT", title))
    story.append(Spacer(1, 12))

    story.append(
        Paragraph(
            f"<b>Generated:</b> {datetime.now().strftime('%d %B %Y %H:%M')}",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>Dataset:</b> {dataset_name}",
            normal
        )
    )

    story.append(Spacer(1, 10))

    story.append(HRFlowable(width="100%"))

    story.append(Spacer(1, 10))

    # Build report

    for line in report_text.split("\n"):

        line = line.strip()

        if not line:
            continue

        # remove markdown bold
        line = line.replace("**", "")

        # Remove markdown bullets
        line = re.sub(r"^\*\s*", "• ", line)

        headings = [
            "Executive Summary",
            "Business Insights",
            "Risks",
            "Opportunities",
            "Recommendations"
        ]

        if line.lower() in [h.lower() for h in headings]:

            story.append(Spacer(1, 8))

            story.append(HRFlowable(width="100%"))

            story.append(Spacer(1, 8))

            story.append(Paragraph(line.upper(), heading))
            story.append(Spacer(1, 6))

        else:

            story.append(Paragraph(line, normal))

    doc.build(story)

    return pdf_path