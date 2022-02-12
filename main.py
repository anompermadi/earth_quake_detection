"""
Earth Quake Detection App
"""
import last_earthquake

if __name__ == '__main__':
    print("Main Application")
    result = last_earthquake.data_extraction()
    last_earthquake.show_data(result)
