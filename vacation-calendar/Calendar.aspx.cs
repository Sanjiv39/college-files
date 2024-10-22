using Vacation;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Reflection.Emit;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;


namespace Vacation
{
    public partial class Calendar : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void SelectionChanged(object sender, EventArgs e)
        {
            string i = "Your Selected Date:" + Calendar1.SelectedDate.Date.ToString();
        }

        protected void btnResult_Click(object sender, EventArgs e)
        {
            Calendar1.Caption = "SAMBARE";
            Calendar1.FirstDayOfWeek = FirstDayOfWeek.Sunday;
            Calendar1.NextPrevFormat = NextPrevFormat.ShortMonth;
            Calendar1.TitleFormat = TitleFormat.Month;
            Label2.Text = "Todays Date" + Calendar1.TodaysDate.ToShortDateString();
            Label3.Text = "Ganpati Vacation Start: 9-13-2018";
            if (Calendar1.SelectedDate.ToShortDateString() == "9-13-2018")
                Label3.Text = "<b>Ganpati Festival Start</b>";
            if (Calendar1.SelectedDate.ToShortDateString() == "9-23-2018")
                Label3.Text = "<b>Ganpati Festival End</b>";
        }
        protected void Calendar1_DayRender(object sender, System.Web.UI.WebControls.DayRenderEventArgs e)
        {
            if (e.Day.Date.Day == 5 && e.Day.Date.Month == 9)
            {
                System.Web.UI.WebControls.Label lbl = new System.Web.UI.WebControls.Label();
                e.Cell.BackColor = System.Drawing.Color.Yellow;
                lbl.Text = "<br>Teachers Day!";
                e.Cell.Controls.Add(lbl);
            }

            if (e.Day.Date.Day == 13 && e.Day.Date.Month == 9)
            {
                Calendar1.SelectedDate = new DateTime(2018, 9, 12);
                Calendar1.SelectedDates.SelectRange(Calendar1.SelectedDate,
                Calendar1.SelectedDate.AddDays(10));
                System.Web.UI.WebControls.Label lbl1 = new System.Web.UI.WebControls.Label();
                lbl1.Text = "<br>Ganpati!";
                e.Cell.Controls.Add(lbl1);
            }
        }
        protected void btnReset_Click(object sender, EventArgs e)
        {
            Label1.Text = "";
            Label2.Text = "";
            Label3.Text = "";
            Label4.Text = "";
            Label5.Text = "";
            Calendar1.SelectedDates.Clear();
        }
    }
}