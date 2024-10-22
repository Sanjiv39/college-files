using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Emit;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace project_1.states.session
{
    public partial class Second : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            if (Session["user"] == null)
            {
                Response.Redirect("First.aspx");
            }
            else
            {
                Label1.Text = "HELLO " + Session["user"];
            }
        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            Session["course"] = DropDownList1.SelectedItem;
            Response.Redirect("Third.aspx");
        }
    }
}