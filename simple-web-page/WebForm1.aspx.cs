using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
namespace WebApplication1
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
        }
        protected void SelectedIndexChanged(object sender, EventArgs e)
        {
            Console.WriteLine(DropDownList1.SelectedIndex.ToString());
        }
        protected void Button1_Click(object sender, EventArgs e)
        {
            string s;
            if (RadioButton1.Checked == true)
            {
                s = RadioButton1.Text;
            }
            else if (RadioButton2.Checked == true)
            {
                s = RadioButton1.Text;
}
            else
            {
                s = RadioButton3.Text;
            }
            Label5.Text = "You have been enrolled in " + DropDownList1.SelectedItem; Label5.Text += " in " + s;
        }
    }
}