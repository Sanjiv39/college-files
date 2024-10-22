using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace project_1.states.session
{
    public partial class Third : System.Web.UI.Page
    {
        protected void PREV_Click(object sender, EventArgs e)
        {
            if (Session["user"] == null || Session["pswd"] == null)
            {
                Response.Redirect("First.ASPX");
            }
            else
            {
                //Label1.Text = Session["course"].ToString();
                Response.Redirect("Second.ASPX");
            }
        }
        protected void LOGOUT_Click(object sender, EventArgs e)
        {
            Response.Redirect("Fourth.aspx");
        }
    }
}