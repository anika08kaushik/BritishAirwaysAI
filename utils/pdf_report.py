from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from datetime import datetime


def generate_pdf(
    filename,
    review,
    sentiment,
    quality,
    recommendations,
    aspects
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    title_style.alignment = TA_CENTER

    story = []

    # -------------------------------------------------
    # Title
    # -------------------------------------------------

    story.append(
        Paragraph(
            "British Airways AI Review Analysis Report",
            title_style
        )
    )

    story.append(Spacer(1,0.3*inch))

    story.append(

        Paragraph(

            f"<b>Generated :</b> {datetime.now().strftime('%d %B %Y %I:%M %p')}",

            styles["Normal"]

        )

    )

    story.append(Spacer(1,0.2*inch))

    # -------------------------------------------------
    # Summary
    # -------------------------------------------------

    summary = [

        ["Predicted Sentiment", sentiment],

        ["Review Quality Score", f"{quality}/100"]

    ]

    table = Table(summary,colWidths=[180,250])

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,0),(0,-1),colors.whitesmoke),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8)

        ])

    )

    story.append(table)

    story.append(Spacer(1,0.3*inch))

    # -------------------------------------------------
    # Customer Review
    # -------------------------------------------------

    story.append(

        Paragraph(

            "<b>Customer Review</b>",

            styles["Heading2"]

        )

    )

    story.append(

        Paragraph(

            review,

            styles["BodyText"]

        )

    )

    story.append(Spacer(1,0.2*inch))

    # -------------------------------------------------
    # Aspect Analysis
    # -------------------------------------------------

    story.append(

        Paragraph(

            "<b>Aspect Analysis</b>",

            styles["Heading2"]

        )

    )

    data = [

        [

            "Aspect",

            "Rating",

            "Status"

        ]

    ]

    for _, row in aspects.iterrows():

        data.append([

            row["Aspect"],

            "⭐"*row["Rating"],

            row["Status"]

        ])

    table = Table(data,colWidths=[170,120,140])

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,1),(-1,-1),colors.beige),

            ("ALIGN",(0,0),(-1,-1),"CENTER"),

            ("BOTTOMPADDING",(0,0),(-1,-1),8),

            ("TOPPADDING",(0,0),(-1,-1),8)

        ])

    )

    story.append(table)

    story.append(Spacer(1,0.3*inch))

    # -------------------------------------------------
    # AI Recommendation
    # -------------------------------------------------

    story.append(

        Paragraph(

            "<b>AI Recommendation</b>",

            styles["Heading2"]

        )

    )

    recommendation = recommendations.replace("\n","<br/>")

    story.append(

        Paragraph(

            recommendation,

            styles["BodyText"]

        )

    )

    story.append(Spacer(1,0.3*inch))

    # -------------------------------------------------
    # Footer
    # -------------------------------------------------

    story.append(

        Paragraph(

            "<i>Generated automatically using Logistic Regression, Amazon Bedrock, AWS Lambda and Amazon DynamoDB.</i>",

            styles["Italic"]

        )

    )

    doc.build(story)