import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private ImageView imageView;
    private Button changeImageButton;
    private boolean isImage1 = true;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        imageView = findViewById(R.id.imageView);
        changeImageButton = findViewById(R.id.changeImageButton);

        // Set the initial background image
        setInitialImage();

        changeImageButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Change the background image on each button click
                toggleImage();
            }
        });
    }

    private void setInitialImage() {
        // Set the initial background image (image1.jpg)
        imageView.setBackgroundResource(R.drawable.image1);
    }

    private void toggleImage() {
        // Change the background image on each button click
        if (isImage1) {
            imageView.setBackgroundResource(R.drawable.image2);
        } else {
            imageView.setBackgroundResource(R.drawable.image1);
        }

        // Toggle the flag for the next click
        isImage1 = !isImage1;
    }
}
