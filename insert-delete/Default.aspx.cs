using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data.SqlClient;
using System.Net;
using System.Security.Cryptography;
using System.Xml.Linq;

namespace project_1.insert_delete
{
    public partial class Default : System.Web.UI.Page
    {
        string cs = "data source=DESKTOP-8QHF2UM;initial catalog=college;integrated security=true";
        SqlConnection con;
        protected void Page_Load(object sender, EventArgs e)
        {
            con = new SqlConnection(cs);
            if (IsPostBack == false)
            {
                string q = "select eid from employee";
                SqlCommand cmd = new SqlCommand(q, con);
                con.Open();
                SqlDataReader dr = cmd.ExecuteReader();
                dr.Read();
                DropDownList1.DataSource = dr;
                DropDownList1.DataTextField = "eid";
                DropDownList1.DataBind();
                con.Close();
            }
        }

        protected void btn_insert_Click(object sender, EventArgs e)
        {
            string query = "insert into employee values('" + eid.Text + "','" + ename.Text + "','" + desig.Text + "','" + address.Text + "','" + salary.Text + "')";
            SqlCommand cmd = new SqlCommand(query, con);
            con.Open();
            cmd.ExecuteNonQuery();
            Response.Write("Data Inserted");
            con.Close();
        }
        protected void DropDownList1_SelectedIndexChanged(object sender, EventArgs e)
        {
            string q1 = "select ename from employee where eid='" + DropDownList1.SelectedValue + "'";
            SqlCommand cmd1 = new SqlCommand(q1, con);
            con.Open();
            SqlDataReader dr1 = cmd1.ExecuteReader();
            dr1.Read();
            emp_name.Text = dr1[0].ToString();
            con.Close();
        }
        protected void btn_del_Click(object sender, EventArgs e)
        {
            string q2 = "delete from employee where eid='" + DropDownList1.SelectedValue + "'";
            SqlCommand cmd2 = new SqlCommand(q2, con);
            con.Open();
            cmd2.ExecuteNonQuery();
            Response.Write("record deleted");
            con.Close();
        }
    }
}