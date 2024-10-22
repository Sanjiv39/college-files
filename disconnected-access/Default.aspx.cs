using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data.SqlClient;
using System.Data;

namespace project_1.disconnected_access
{
    public partial class Default : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            string cs = "data source=DESKTOP-16RE47P\\SQLEXPRESS;initial catalog=college1;uid=sa;pwd=deepa123";
            SqlConnection conn = new SqlConnection(cs);
            SqlCommand cmd = new SqlCommand("select * from student", conn);
            SqlDataAdapter da = new SqlDataAdapter(cmd);
            DataSet ds = new DataSet();
            da.Fill(ds);
            GridView1.DataSource = ds;
            GridView1.DataBind();
        }
    }
}