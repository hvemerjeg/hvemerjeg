/*For an explanation of the algorithm please go to the python version of the algorithm*/
function validSubSequence(arr, s) {
	arr_index = 0;
	s_index = 0;
	while (arr_index < arr.length && s_index < s.length) {
		if (s[s_index] == arr[arr_index]) {
			s_index++;
		}
		arr_index++;
	}
	return s_index == s.length;
}
