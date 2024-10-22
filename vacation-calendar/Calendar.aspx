<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Calendar.aspx.cs" Inherits="Vacation.Calendar"%>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <asp:Calendar ID="Calendar1" runat="server" BackColor="#FFFFCC" BorderColor="#FFCC66" BorderWidth="1px"
        DayNameFormat="Shortest" Font-Names="Verdana" Font-Size="8pt" ForeColor="#663399" Height="200px"
        NextPrevFormat="ShortMonth" OnDayRender="DayRender" ShowGridLines="True" Width="300px"
        OnSelectionChanged="SelectionChanged">
        <DayHeaderStyle BackColor="#FFCC66" Font-Bold="True" Height="1px" />
        <NextPrevStyle BorderStyle="Solid" BorderWidth="2px" Font-Size="9pt"
            ForeColor="#FFFFCC" />
        <OtherMonthDayStyle BackColor="#FFCC99" BorderStyle="Solid"
            ForeColor="#CC9966" />
        <SelectedDayStyle BackColor="Red" Font-Bold="True" />
        <SelectorStyle BackColor="#FFCC66" />
        <TitleStyle BackColor="#990000" Font-Bold="True" Font-Size="9pt"
            ForeColor="#FFFFCC" />
        <TodayDayStyle BackColor="#FFCC66" ForeColor="White" />
        <WeekendDayStyle Height="50px" />
    </asp:Calendar>
</body>
</html>
