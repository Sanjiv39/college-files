<%@ Control Language="C#" AutoEventWireup="true" %>
CodeFile="UserControl.ascx.cs" Inherits="UserControl.Control" %>
<h3>This is User Contro1 </h3>
<table>
    <tr>
        <td>Name</td>
        <td>
            <asp:TextBox ID="txtName" runat="server"></asp:TextBox>
        </td>
    </tr>
    <tr>
        <td>City</td>
        <td>
            <asp:TextBox ID="txtcity" runat="server"></asp:TextBox></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>
            <asp:Button ID="txtSave" runat="server" Text="Save" OnClick="txtSave" />
        </td>
    </tr>
</table>
<br />
<asp:Label ID="Label1" runat="server" ForeColor="White" Text=" "></asp:Label>