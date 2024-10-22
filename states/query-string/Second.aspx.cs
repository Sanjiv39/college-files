using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace project_1.states.query_string
{
    public partial class Second : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            string n = Request.QueryString["name"];
            TextBox1.Text = n;
            TextBox2.Text = Request.QueryString["course"];
        }
    }
}