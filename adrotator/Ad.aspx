<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Ad.aspx.cs" Inherits="project_1.adrotator.Ad" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <asp:AdRotator ID="AdRotator1" runat="server" DataSourceID="XmlDataSource1" />
    <asp:XmlDataSource ID="XmlDataSource1" runat="server"
        DataFile="~/Ad.xml"></asp:XmlDataSource>
</body>
</html>
