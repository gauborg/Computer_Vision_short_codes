if not badlines:
#             self.left_fit = np.polyfit(lefty, leftx, 2)
#             self.right_fit = np.polyfit(righty, rightx, 2)
            t_left_fit = np.polyfit(lefty, leftx, 2)
            t_right_fit = np.polyfit(righty, rightx, 2)            

        # Generate x and y values for plotting
#         ploty = np.linspace(0, self.binary_warped.shape[0]-1, self.binary_warped.shape[0] )
#         try:
#             left_fitx = self.left_fit[0]*self.ploty**2 + self.left_fit[1]*self.ploty + self.left_fit[2]
#             right_fitx = self.right_fit[0]*self.ploty**2 + self.right_fit[1]*self.ploty + self.right_fit[2]
        left_fitx = t_left_fit[0]*self.ploty**2 + t_left_fit[1]*self.ploty + t_left_fit[2]
        right_fitx = t_right_fit[0]*self.ploty**2 + t_right_fit[1]*self.ploty + t_right_fit[2]