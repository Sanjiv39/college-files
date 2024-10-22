using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace project_1.states.session
{
    public partial class First : System.Web.UI.Page
    {
        protected void On_Login(object sender, EventArgs e)
        {
            if (TextBox1.Text == "sahyog" && TextBox2.Text == "sahyog123")
            {
                Session["user"] = TextBox1.Text;
                Session["pswd"] = TextBox2.Text;
                Response.Redirect("Second.aspx");
            }
            else
            {
                TextBox1.Focus();
            }
        }
    }
}