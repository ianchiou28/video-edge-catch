import cv2
import os

def main():


    video_path = 'name.mp4'#输入视频位置
    output_dir = 'processed_frames'
    output_video_name = 'processed_edges.mp4'

    os.makedirs(output_dir, exist_ok=True)

    try:

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"无法开启档案: {video_path}")
            return


        fps = cap.get(cv2.CAP_PROP_FPS)
        delay = int(1000 / fps)
        original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        scale_factor = 1.2

        image_paths = []

        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error")
                break

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray_frame, 100, 200)
            resized_edges = cv2.resize(edges, dsize=(int(original_width * scale_factor),
                                                     int(original_height * scale_factor)))

            frame_count += 1

            cv2.imshow('Canny Edges', resized_edges)

            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

    except Exception as e:
        print("Error:", e)

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()