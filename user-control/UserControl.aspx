<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="UserControl.aspx.cs" Inherits="project_1.user_control.UserControl" %>

<%@ Register Src="UserControl.ascx" TagPrefix="uc" TagName="Student" %>
<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <uc:Student ID="studentcontrol" runat="server" />
        </div>
    </form>
</body>
</html>
