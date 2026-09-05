
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
