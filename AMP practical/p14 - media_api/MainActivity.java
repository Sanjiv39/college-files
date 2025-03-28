package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    private MediaPlayer mediaPlayer;
    private Button playButton;
    private boolean isPlaying = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        playButton = findViewById(R.id.playButton);
        mediaPlayer = MediaPlayer.create(this, R.drawable.sample);

        playButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (isPlaying) {
                    // If currently playing, stop the audio
                    stopAudio();
                } else {
                    // If not playing, start playing the audio
                    playAudio();
                }
            }
        });

    }

    private void playAudio() {
        mediaPlayer.start();
        isPlaying = true;
        playButton.setText("Pause");
    }

    private void stopAudio() {
        mediaPlayer.pause();
        mediaPlayer.seekTo(0); // Rewind to the beginning
        isPlaying = false;
        playButton.setText("Play");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (mediaPlayer != null) {
            mediaPlayer.release(); // Release the MediaPlayer when the activity is destroyed
        }
    }
}
