import csv
import json
import fpdf


def main(company,position,skills=None,hiring_manager=None):

    pdf=fpdf.FPDF('P','mm','A4')
    pdf.add_page()
    pdf.set_font('Arial','',10)

    cover_letter_head=open('cover_letter_header.txt','r')
    for line in cover_letter_head:
        line = line.replace('#company','{}'.format(company))
        line = line.replace('#position',position)
        pdf.write(6,line)

    pdf.set_font('Arial','B',10)
    pdf.cell(6,6,'What you are looking for:',border=0)
    pdf.cell(80)
    pdf.cell(6,6, 'What I will offer:', border=0)

    pdf.set_font('Arial', '', 10)
    for skill in skills:
        pdf.ln('6')
        pdf.cell(10)
        skill_ask=open('skills/{}.txt'.format(skill),'r').read().replace('\n',' ')
        pdf.cell(6,6,skill_ask,border=0)
        pdf.cell(80)
        skill_exp=open('my_experience/{}.txt'.format(skill),'r').read().replace('\n',' ')
        pdf.multi_cell(90, 6, skill_exp, border=0)

    pdf.ln('6')
    cover_letter_footer = open('cover_letter_footer.txt', 'r')
    for line in cover_letter_footer:
        line = line.replace('#company', company)
        pdf.write(6,line)


    pdf.output('cover letter for {} by Zhanren.pdf'.format(position),'F')
    pdf.close()

    return True

if __name__ == "__main__":
    company='Affirm'
    position='Senior Business Intelligence Analyst'
    skills=['SQL','python','data_visualization']

    main(company,position,skills=skills)