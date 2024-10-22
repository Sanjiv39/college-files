<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="project_1.bootstrap.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <link href="Content/bootstrap.min.css" rel="stylesheet" />
    <script src="Scripts/bootstrap.bundle.js"></script>
    <script src="Scripts/bootstrap.min.js"></script>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:Button ID="Button1" runat="server" Text="primary" class="btn btn-primary" />
            <asp:Button ID="Button2" runat="server" Text="danger" class="btn btn-danger" />
            <asp:Button ID="Button3" runat="server" Text="secondary" class="btn btn-secondary" />
            <asp:Button ID="Button4" runat="server" Text="success" class="btn btn-success" />
            <asp:Button ID="Button5" runat="server" Text="warning" class="btn btn-warning" />
            <asp:Button ID="Button6" runat="server" Text="info" class="btn btn-info" />
            <asp:Button ID="Button7" runat="server" Text="light" class="btn btn-light" />
            <asp:Button ID="Button8" runat="server" Text="dark" class="btn btn-dark" />
            <button type="button" class="btn btn-link">Link</button>
            <br />
            <br />
            <button type="button" class="btn btn-outline-primary">Primary</button>
            <button type="button" class="btn btn-outline-secondary">Secondary</button>
            <button type="button" class="btn btn-outline-success">Success</button>
            <button type="button" class="btn btn-outline-danger">Danger</button>
            <button type="button" class="btn btn-outline-warning">Warning</button>
            <button type="button" class="btn btn-outline-info">Info</button>
            <button type="button" class="btn btn-outline-light">Light</button>
            <button type="button" class="btn btn-outline-dark">Dark</button>
        </div>
    </form>
</body>
</html>
