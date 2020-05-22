#!/usr/bin/python
__author__ = "Nognut"
#writting into an html file.
with open("new_html.html", "w") as file:

    #stylings to give border to the table elements
    styles = """
    <style >
        table, th, td{
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td{
            padding: 5px ;
            text-align: left;
        }
    </style >
    """
    file.write(styles)

    #defining the styles of the table
    tr_style = "background-color:rgb(206,202,202);"
    table_style = "width:50%;background-color:rgb(124,197,197);"

    file.write("<table style={}>\n".format(table_style))  # table opening tag

    #defining the heading of the table
    file.write(" <tr style={}>\n".format(tr_style))  # <tr></tr> -> table row
    file.write("    <th>Firstname </th>\n")  # this is heading
    file.write("    <th>LastName </th>\n")  # this is heading
    file.write("    <th>PhoneNo. </th>\n")  # this is heading
    file.write(" </tr>\n")

    #writing into the table boxes.
    file.write(" <tr>\n")
    file.write("    <td>Tungon</td>\n")  # <td></td> -> is for table data.
    file.write("    <td>Dugi</td>\n")
    file.write("    <td>7640947892</td>\n")
    file.write(" </tr>\n")

    file.write(" <tr>\n")
    file.write("    <td>Gerish</td>\n")  # <td></td> -> is for table data.
    file.write("    <td>Dugi</td>\n")
    file.write("    <td>76445687892</td>\n")
    file.write(" </tr>\n")

    file.write(" <tr>\n")
    file.write("    <td>Nehru</td>\n")  # <td></td> -> is for table data.
    file.write("    <td>Dugi</td>\n")
    file.write("    <td>75566947892</td>\n")
    file.write(" </tr>\n")

    file.write(" <tr>\n")
    file.write("    <td>Manshi</td>\n")  # <td></td> -> is for table data.
    file.write("    <td>Dugi</td>\n")
    file.write("    <td>76409789522</td>\n")
    file.write(" </tr>\n")

    file.write(" <tr>\n")
    file.write("    <td>Anjali</td>\n")  # <td></td> -> is for table data.
    file.write("    <td>Dugi</td>\n")
    file.write("    <td>7640941513</td>\n")
    file.write(" </tr>\n")

    file.write("</table>\n")  # table closing tab
