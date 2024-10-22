<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %>

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .style1 {
            width: 100%;
        }

        .style2 {
            width: 153px;
        }

        .style3 {
            width: 153px;
            height: 26px;
        }

        .style4 {
            height: 26px;
        }

        .auto-style1 {
            width: 153px;
            height: 28px;
        }

        .auto-style2 {
            height: 28px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <table class="style1">
                <tr>
                    <td class="style2">
                        <asp:Label ID="Label1" runat="server" Text="Roll No">
                        </asp:Label>
                    </td>
                    <td>
                        <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
                    </td>
                </tr>
                <tr>
                    <td class="style2">
                        <asp:Label ID="Label2" runat="server" Text="Name">
                        </asp:Label></td>
                    <td>
                        <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
                    </td>
                </tr>
                <tr>
                    <td class="auto-style1">Class</td>
                    <td class="auto-style2">
                        <asp:RadioButton ID="RadioButton1" runat="server" Text="FY" GroupName="class"/>
                        <asp:RadioButton ID="RadioButton2" runat="server" Text="SY" GroupName="class"/>
                        <asp:RadioButton ID="RadioButton3" runat="server" Text="TY" GroupName="class"/>
                    </td>
                </tr>
                <tr>
                    <td class="style3">
                        <asp:Label ID="Label4" runat="server" Text="Course"></asp:Label>
                    </td>
                    <td class="style4">
                        <asp:DropDownList ID="DropDownList1" runat="server">
                            <asp:ListItem>B.Com</asp:ListItem>
                            <asp:ListItem>BMS</asp:ListItem>
                            <asp:ListItem>B.SC(IT)</asp:ListItem>
                            <asp:ListItem>B.Sc(CS)</asp:ListItem>
                        </asp:DropDownList>
                    </td>
                </tr>
                <tr>
                    <td class="style3">&nbsp;</td>
                    <td class="style4">
                        <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="Button" />
                    </td>
                </tr>
            </table>
        </div>
        <asp:Label ID="Label5" runat="server" Text="Label"></asp:Label>
    </form>
</body>
</html>
