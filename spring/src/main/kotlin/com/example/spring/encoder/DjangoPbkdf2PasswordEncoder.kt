package com.example.spring.encoder

import org.springframework.security.crypto.keygen.BytesKeyGenerator
import org.springframework.security.crypto.keygen.KeyGenerators
import org.springframework.security.crypto.password.PasswordEncoder
import java.security.GeneralSecurityException
import java.security.MessageDigest
import java.util.*
import javax.crypto.SecretKeyFactory
import javax.crypto.spec.PBEKeySpec

class DjangoPbkdf2PasswordEncoder : PasswordEncoder {

    companion object {
        private const val PREFIX = "pbkdf2_sha256"
        private const val SEPARATOR = "\$"
        private const val ITERATIONS = 180000
        private const val HASH_WIDTH = 256
        private const val ALGORITHM = "PBKDF2WithHmacSHA256"
    }

    private val saltGenerator: BytesKeyGenerator = KeyGenerators.secureRandom()

    private fun base64Decode(string: String): ByteArray {
        return Base64.getDecoder().decode(string)
    }

    private fun base64Encode(bytes: ByteArray): String {
        return Base64.getEncoder().encodeToString(bytes)
    }

    override fun encode(rawPassword: CharSequence): String {
        val salt = saltGenerator.generateKey()
        val hash = encodeWithSalt(rawPassword, salt)

        val encodedHash = base64Encode(hash)
        val encodedSalt = base64Encode(salt)

        return listOf(PREFIX, ITERATIONS, encodedSalt, encodedHash).joinToString(SEPARATOR)
    }

    private fun encodeWithSalt(rawPassword: CharSequence, salt: ByteArray): ByteArray {
        return encodeWithSaltAndIterations(rawPassword, salt, ITERATIONS)
    }

    private fun encodeWithSaltAndIterations(rawPassword: CharSequence, salt: ByteArray, iterations: Int): ByteArray {
        val keySpec = PBEKeySpec(
            rawPassword.toString().toCharArray(),
            salt,
            iterations,
            HASH_WIDTH
        )

        return try {
            SecretKeyFactory.getInstance(ALGORITHM)
                .generateSecret(keySpec)
                .encoded
        } catch (e: GeneralSecurityException) {
            throw IllegalStateException("Could not create hash", e)
        }
    }

    override fun matches(rawPassword: CharSequence, partsEncodedPassword: String): Boolean {
        if (!partsEncodedPassword.startsWith(PREFIX)) {
            throw IllegalArgumentException("Encoded password does not start with: $PREFIX")
        }

        val parts = partsEncodedPassword.split(SEPARATOR)
        if (parts.size != 4) {
            throw IllegalArgumentException("The encoded password format does not have 4 parts")
        }

        val iterations = parts[1].toInt()
        val salt = base64Decode(parts[2])
        val hash = base64Decode(parts[3])

        return MessageDigest.isEqual(
            hash,
            encodeWithSaltAndIterations(rawPassword, salt, iterations)
        )
    }
}