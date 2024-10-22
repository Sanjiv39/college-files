<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Home.aspx.cs" Inherits="sitemap.Home" %>

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:SiteMapPath ID="SiteMapPath1" runat="server" RenderCurrentNodeAsLink="True" ParentLevelsDisplayed="3">
            </asp:SiteMapPath>
            <h1>home page</h1>
        </div>
    </form>
</body>
</html>
