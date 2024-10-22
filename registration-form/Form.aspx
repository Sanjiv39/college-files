<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Form.aspx.cs" Inherits="project_1.registration_form.Form" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="f1" method="post" runat="server">
        <fieldset style="width: 280px">
            <legend>Registration Form</legend>
            <table>
                <tr>
                    <td>First Name:</td>
                    <td>
                        <asp:TextBox ID="txt1" runat="server"></asp:TextBox></td>
                    <td>
                        <asp:RequiredFieldValidator ID="validfname" runat="server" ControlToValidate="txt1" ErrorMessage="Required!" ForeColor="Red"></asp:RequiredFieldValidator></td>
                </tr>
                <tr>
                    <td>Last Name:</td>
                    <td>
                        <asp:TextBox ID="txt2" runat="server"></asp:TextBox></td>
                    <td>
                        <asp:RequiredFieldValidator ID="validlname" runat="server" ControlToValidate="txt2" ErrorMessage="Required!" ForeColor="Red"></asp:RequiredFieldValidator></td>
                </tr>
                <tr>
                    <td>User Name:</td>
                    <td>
                        <asp:TextBox ID="user" runat="server"></asp:TextBox></td>
                    <td>
                        <asp:RequiredFieldValidator ID="validuser" runat="server" ControlToValidate="user" ErrorMessage="Required!" ForeColor="Red"></asp:RequiredFieldValidator></td>
                </tr>
                <tr>
                    <td>Password:</td>
                    <td>
                        <asp:TextBox ID="pwd" runat="server" TextMode="Password"></asp:TextBox></td>
                    <td>
                        <asp:RequiredFieldValidator ID="validpwd" runat="server" ControlToValidate="pwd" ErrorMessage="Required!" ForeColor="Red"></asp:RequiredFieldValidator></td>
                </tr>
                <tr>
                    <td>Confirm Password:</td>
                    <td>
                        <asp:TextBox ID="Textbox1" runat="server" TextMode="Password"></asp:TextBox></td>
                </tr>
                <tr>
                    <td>Email:</td>
                    <td>
                        <asp:TextBox ID="email" runat="server" TextMode="Email"></asp:TextBox></td>
                    <td>
                        <asp:RequiredFieldValidator ID="validemail" runat="server" ControlToValidate="email" ErrorMessage="required!" ForeColor="Red"></asp:RequiredFieldValidator></td>
                </tr>
                <tr>
                    <td>Mobile:</td>
                    <td>
                        <asp:TextBox ID="mobile" runat="server" TextMode="Phone"></asp:TextBox></td>
                </tr>
                <tr>
                    <td>Gender:</td>
                    <td>
                        <asp:RadioButtonList ID="RadioButtonList1" runat="server">
                            <asp:ListItem Text="Male" Value="0"></asp:ListItem>
                            <asp:ListItem Text="Female" Value="1"></asp:ListItem>
                        </asp:RadioButtonList></td>
                </tr>
                <tr>
                    <td>DOB: </td>
                    <td>
                        <asp:TextBox ID="dob" runat="server" TextMode="Date" Width="168px"></asp:TextBox>
                    </td>
                    <td>
                        <asp:RequiredFieldValidator ID="validdob" runat="server" ControlToValidate="dob" ErrorMessage="Required" ForeColor="Red"></asp:RequiredFieldValidator></td>
                </tr>
                <tr>
                    <td>Course: </td>
                    <td>
                        <asp:DropDownList ID="ddlCourse" runat="server" DataValueField="Course" Width="173px">
                            <asp:ListItem Text="Select Course" Value="-1"></asp:ListItem>
                            <asp:ListItem Text="BTech" Value="0"></asp:ListItem>
                            <asp:ListItem Text="MCA" Value="1"></asp:ListItem>
                            <asp:ListItem Text="MBA" Value="2"></asp:ListItem>
                        </asp:DropDownList></td>
                    <td>
                        <asp:RequiredFieldValidator InitialValue="-1" ID="validcourse" runat="server" ControlToValidate="ddlCourse" ErrorMessage="Required!" ForeColor="Red"></asp:RequiredFieldValidator></td>
                </tr>
                <tr>
                    <td>Nationality:</td>
                    <td>
                        <asp:CheckBox ID="check" Text="Indian" runat="server" /><asp:CheckBox ID="checkNat" Text="Others" runat="server" /></td>
                </tr>
                <tr>
                    <td>Profile: </td>
                    <td>
                        <asp:Image ID="img" ImageUrl="images/new/new-member.png" runat="server" /></td>
                </tr>
                <tr>
                    <td></td>
                    <td>
                        <asp:FileUpload ID="imgupload" runat="server" Enabled="true" /></td>
                </tr>
                <tr>
                    <td>
                        <asp:Button ID="btn1" runat="server" Text="Submit"></asp:Button></td>
                    <td>
                        <asp:Button ID="btn2" runat="server" Text="Reset"></asp:Button></td>
                </tr>
            </table>
        </fieldset>
    </form>
</body>
</html>
