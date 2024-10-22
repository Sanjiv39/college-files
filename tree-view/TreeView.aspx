<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="TreeView.aspx.cs" Inherits="WebTree.TreeView" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <asp:TreeView ID="TreeView1" runat="server" ShowLines="True" ForeColor="#CC0000" PathSeparator="&lt;">
        <Nodes>
            <asp:TreeNode Text="home" Value="New Node" NavigateUrl="~/HOME.aspx">
                <asp:TreeNode NavigateUrl="~/ABOUT.aspx" Text="ABOUT" Value="ABOUT"></asp:TreeNode>
                <asp:TreeNode Text="coures" Value="New Node" NavigateUrl="~/course.aspx">
                    <asp:TreeNode Text="BCA" Value="New Node" NavigateUrl="~/BCA.aspx"></asp:TreeNode>
                    <asp:TreeNode NavigateUrl="~/BBA.aspx" Text="BBA" Value="BBA"></asp:TreeNode>
                </asp:TreeNode>
                <asp:TreeNode Text="ADDRESS" Value="ADDRESS" NavigateUrl="~/ADDRESS.aspx"></asp:TreeNode>
            </asp:TreeNode>
        </Nodes>
    </asp:TreeView>
</body>
</html>
