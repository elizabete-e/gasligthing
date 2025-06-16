import { View, Text, StyleSheet } from 'react-native'
import React from 'react'

const closet = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Closet</Text>
    </View>
  )
}

export default closet

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: "center",
    alignItems: "center",
  },
  text: {
    color: 'white',
    fontSize: 42,
    fontWeight: "bold",
    textAlign: "center",


  }
})