import { createSlice } from '@reduxjs/toolkit';

const interactionsSlice = createSlice({
  name: 'interactions',
  initialState: { items: [] },
  reducers: {
    addInteraction(state, action) {
      state.items.push(action.payload);
    },
  },
});

export const { addInteraction } = interactionsSlice.actions;
export default interactionsSlice.reducer;